from google.cloud import bigquery
import os
import csv
from dotenv import load_dotenv

load_dotenv()

service_account_json_path = os.environ["GCP_SERVICE_ACCOUNT_PATH"]
csv_file_path = "./02_05_big_query/sample.csv"
dataset_name = os.environ["BQ_DATASET_NAME"]
table_name = os.environ["BQ_TABLE_NAME"]

bigquery_client = bigquery.Client.from_service_account_json(service_account_json_path)

def write_data(dataset_name, table_name, data):
    print ("writing data into", dataset_name, table_name, data)
    dataset_ref = bigquery_client.dataset(dataset_name)
    table_ref = dataset_ref.table(table_name)
    table = bigquery_client.get_table(table_ref)
    errors = bigquery_client.insert_rows(table, data)
    if errors:
        print (errors)
    else:
        print ("new rows are added")
    
    


def read_csv(csv_file_path):
    with open(csv_file_path, "r") as f:
        reader = csv.reader(f, delimiter=",")
        # Removing the header
        data = list(reader)[1:]
    return data


data = read_csv(csv_file_path)
print(data)
write_data(dataset_name, table_name, data)
