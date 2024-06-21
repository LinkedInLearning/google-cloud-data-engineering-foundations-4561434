from google.cloud import bigquery
import os
import json
from dotenv import load_dotenv, find_dotenv

# clean os environment
os.environ.clear()
load_dotenv(find_dotenv())

print (os.environ)

service_account_json_path = os.environ["GCP_SERVICE_ACCOUNT_PATH"]

try:
    with open(service_account_json_path, "r") as f:
        service_account_json = json.load(f)
except FileNotFoundError:
    print("Service account JSON file not found. Did you download the file and set the GCP_SERVICE_ACCOUNT_PATH environment variable?")
    exit()
except json.JSONDecodeError:
    print("Check if the service account JSON file is a valid JSON")
    exit()

bigquery_client = bigquery.Client.from_service_account_info(service_account_json)
