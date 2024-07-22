from google.cloud import bigquery
import os
from dotenv import load_dotenv

load_dotenv()

service_account_json_path = os.environ["GCP_SERVICE_ACCOUNT_PATH"]
dataset_name = os.environ["BQ_DATASET_NAME"]
table_name = os.environ["BQ_TABLE_NAME"]

bigquery_client = bigquery.Client.from_service_account_json(service_account_json_path)


def create_data_set(dataset_name):
    dataset_id = f"{bigquery_client.project}.{dataset_name}"
    dataset = bigquery.Dataset(dataset_id)
    dataset = bigquery_client.create_dataset(dataset, exists_ok=True)
    print (f"The dataset is created : {dataset_id}")
    


def create_table(dataset_name, table_name, schema):
    dataset_ref = bigquery_client.dataset(dataset_name)
    table_ref = dataset_ref.table(table_name)

    table = bigquery.Table(table_ref, schema)
    table = bigquery_client.create_table(table)
    print ("table is created", table_name)


create_data_set(dataset_name)
schema = [
    bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("date_of_birth", "DATE", mode="REQUIRED"),
]
create_table(dataset_name, table_name, schema)
