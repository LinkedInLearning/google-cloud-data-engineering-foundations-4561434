from client import storage_client
import os

bucket_name = os.environ["GCS_BUCKET_NAME"]
if not bucket_name:
    print("GCS_BUCKET_NAME environment variable not set")
    exit()

print ("reading from bucket: ", bucket_name)

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "File {} downloaded to {}.".format(
            source_blob_name, destination_file_name
        )
    )


download_blob(bucket_name, "02_02_cloud_storage/sample.csv", "sample.csv")