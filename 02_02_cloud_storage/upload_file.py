from client import storage_client
import os

bucket_name = os.environ["GCS_BUCKET_NAME"]
if not bucket_name:
    print("GCS_BUCKET_NAME environment variable not set")
    exit()

print ("reading from bucket: ", bucket_name)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

upload_blob(bucket_name, "./02_02_cloud_storage/sample.csv", "02_02_cloud_storage/sample.csv")