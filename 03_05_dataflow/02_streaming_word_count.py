# pytype: skip-file

import argparse
import logging
import os

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.examples.wordcount_with_metrics import WordExtractingDoFn
from apache_beam.transforms import window
# from dotenv import load_dotenv

# os.environ.clear()
# load_dotenv()

# authenticate with serviceaccount json path
service_account_path = os.environ.get("GCP_SERVICE_ACCOUNT_PATH")

if service_account_path:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path


# Count the occurrences of each word.
def count_ones(word_ones):
    (word, ones) = word_ones
    return (word, sum(ones))

# Format the counts into a PCollection of strings.
def format_result(word_count):
    (word, count) = word_count
    return "%s: %s" % (word, count)

def main(argv=None, save_main_session=True):
    """Main entry point; defines and runs the wordcount pipeline."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_topic",
        dest="input_topic",
        required=False,
        default=f"projects/{os.environ['GCP_PROJECT_ID']}/topics/{os.environ.get('WORD_COUNT_TOPIC', 'new-topic')}",
        help="Input PubSub topic of the form '/topics/<PROJECT>/<TOPIC>'",
    )
    parser.add_argument(
        "--output_topic",
        dest="output_topic",
        required=False,
        default=f"projects/{os.environ['GCP_PROJECT_ID']}/topics/{os.environ.get('WORD_COUNT_OUTPUT_TOPIC', 'word-count-output-topic')}",
        help="Output PubSub topic of the form '/topics/<PROJECT>/<TOPIC>'",
    )
    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
    with beam.Pipeline(options=pipeline_options) as p:
        lines = p | beam.io.ReadFromPubSub(topic=known_args.input_topic)

        counts = (
            lines
            | 'convert bytes to string' >> beam.Map(lambda x: x.decode('utf-8'))
            | 'convert to lowercase' >> beam.Map(lambda x: x.lower())
            | "split" >> (beam.ParDo(WordExtractingDoFn()).with_output_types(str))
            | "pair_with_one" >> beam.Map(lambda x: (x, 1))
            | beam.WindowInto(window.FixedWindows(15, 0))
            | "group" >> beam.GroupByKey()
            | "count" >> beam.Map(count_ones)
        )

        output = counts | "format" >> beam.Map(format_result)

        # Write to Pub/Sub
        output | beam.io.WriteStringsToPubSub(known_args.output_topic)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main()
