from google.cloud import storage
import os
from dotenv import load_dotenv

load_dotenv()

service_account_json_path = os.environ["GCP_SERVICE_ACCOUNT_PATH"]
storage_client = storage.Client.from_service_account_json(service_account_json_path)


bucket_name = os.environ["GCS_BUCKET_NAME"]
if not bucket_name:
    print("GCS_BUCKET_NAME environment variable not set")
    exit()

print("reading from bucket: ", bucket_name)


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    try:
        blob.upload_from_filename(source_file_name)
    except Exception as e:
        print(e)
        return

    print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))


upload_blob(
    bucket_name, "./02_03_cloud_storage/sample.csv", "02_03_cloud_storage/sample.csv"
)
