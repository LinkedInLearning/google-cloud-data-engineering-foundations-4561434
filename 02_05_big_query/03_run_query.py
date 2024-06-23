import os

from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()

service_account_json_path = os.environ["GCP_SERVICE_ACCOUNT_PATH"]

bigquery_client = bigquery.Client.from_service_account_json(service_account_json_path)

dataset_name = os.environ["BQ_DATASET_NAME"]
table_name = os.environ["BQ_TABLE_NAME"]


def run_query(query):
    query = bigquery_client.query(query)
    results = query.result()
    return results


query = f"""
SELECT name, age FROM {dataset_name}.{table_name}
"""

results = run_query(query)
print("Query results:")
for row in results:
    print(row)
