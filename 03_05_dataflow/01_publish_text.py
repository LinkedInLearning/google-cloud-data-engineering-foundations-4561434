import os
import json
from google.cloud import pubsub_v1
from dotenv import load_dotenv
from google.api_core.exceptions import AlreadyExists


os.environ.clear()
load_dotenv()


project_id = os.environ["GCP_PROJECT_ID"]
service_account_path = os.environ["GCP_SERVICE_ACCOUNT_PATH"]

publisher = pubsub_v1.PublisherClient.from_service_account_file(service_account_path)
input_topic = f"projects/{os.environ['GCP_PROJECT_ID']}/topics/{os.environ['WORD_COUNT_TOPIC']}"
output_topic = f"projects/{os.environ['GCP_PROJECT_ID']}/topics/{os.environ['WORD_COUNT_OUTPUT_TOPIC']}"

print(project_id, input_topic, output_topic, service_account_path)

def create_topic(topic_name):
    try:
        topic = publisher.create_topic(name=topic_name)
        print(f"Created topic: {topic.name}")
    except AlreadyExists:
        print(f"Topic {topic_name} already exists")
        return


def publish_message(data, topic_name):
    if isinstance(data, str):
        bytes_data = data.encode("utf-8")
    future = publisher.publish(topic_name, bytes_data)
    print(future.result())


if __name__ == "__main__":
    create_topic(input_topic)
    create_topic(output_topic)
    message = input("Enter any message to publish: (exit to quit)")
    while message != "exit":
        publish_message(message, input_topic)
        message = input("Enter any message to publish: (exit to quit)")
