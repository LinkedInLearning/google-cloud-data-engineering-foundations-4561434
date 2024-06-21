from client import bigquery_client
from google.cloud import bigquery
from google.api_core.exceptions import Conflict
import os

dataset_name = os.environ["BQ_DATASET_NAME"]
table_name = os.environ["BQ_TABLE_NAME"]

def create_data_set(dataset_name):
    dataset_id = "{}.{}".format(bigquery_client.project, dataset_name)
    dataset = bigquery.Dataset(dataset_id)
    try:
        dataset = bigquery_client.create_dataset(dataset)
    except Conflict as e:
        print("Dataset already exists")
        return
    print("Created dataset {}.{}".format(bigquery_client.project, dataset.dataset_id))

def create_table(dataset_name, table_name, schema):
    dataset_ref = bigquery_client.dataset(dataset_name)
    table_ref = dataset_ref.table(table_name)

    table = bigquery.Table(table_ref, schema=schema)
    table = bigquery_client.create_table(table)  # API request

    print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))


create_data_set(dataset_name)
schema = [
    bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("date_of_birth", "DATE", mode="REQUIRED"),
]
create_table(dataset_name, table_name, schema)