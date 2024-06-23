# Google BigQuery

This is a simple example of how to create big query tables and run queries using the Google BigQuery API using Python.

## Requirements

1. Check if you've enabled the BigQuery API for your project. If not, enable it.
2. The service account we setup for GCS bucket will be used here as well. So, make sure you have the service account key file.
3. You already have all the necessary python libraries installed. If not, install them using the following command:

```bash
pip install google-cloud-bigquery
```

## Steps

1. To Create a new dataset and table in BigQuery run `python create_table.py`
2. To write data to the table run `python write_data.py`
3. To run a query on the table run `python run_query.py`

Voila! You have successfully created a table in BigQuery and ran a query on it using Python