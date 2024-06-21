from client import bigquery_client
import os

dataset_name = os.environ["BQ_DATASET_NAME"]
table_name = os.environ["BQ_TABLE_NAME"]

def run_query(query):
    query_job = bigquery_client.query(query)
    results = query_job.result()  # Waits for job to complete.
    return results

query = f"""
SELECT name, age FROM {dataset_name}.{table_name}
"""

results = run_query(query)
print ("Query results:")
for row in results:
    print (row)