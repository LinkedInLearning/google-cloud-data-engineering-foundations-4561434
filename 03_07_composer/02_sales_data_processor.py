from airflow import DAG
import os
from airflow.providers.google.cloud.sensors.gcs import (
    GCSObjectExistenceSensor
)
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocSubmitJobOperator
)
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator,
)
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "retries": 0,

}

PROJECT_ID = "gcp-de-foundations"
CLUSTER_NAME = "spark-example-cluster"
SPARK_REGION="us-central1"
JOB_FILE_URI = "gs://de-gcp-example-bucket/03_03_dataproc/scripts/01_pyspark_script.py"
bucket_name = "de-gcp-example-bucket"
source_gcs_path = "03_03_dataproc/sales_data.csv"
processed_gcs_path = "03_06_airflow/processed/sales_data.csv"
# project.dataset.table
big_query_table = f"{PROJECT_ID}:sales_data.sales_data"




PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": JOB_FILE_URI},
}

dag = DAG(
    "sales_data_analysis",
    default_args=default_args,
    description="Sales data analysis",
    schedule_interval=None,
)

new_file_sensor = GCSObjectExistenceSensor(
    task_id="new_file_sensor",
    bucket=bucket_name,
    object=source_gcs_path,
    dag=dag,
)


trigger_spark_job = DataprocSubmitJobOperator(
    task_id="trigger_spark_job",
    job=PYSPARK_JOB,
    region=SPARK_REGION,
    project_id=PROJECT_ID,
    dag=dag,
)

# gs://de-gcp-example-bucket/03_03_dataproc/sales_data.csv
move_file = GCSToGCSOperator(
    task_id="move_file",
    source_bucket=bucket_name,
    source_object=source_gcs_path,
    destination_bucket=bucket_name,
    destination_object=processed_gcs_path,
    move_object=True,
    dag=dag,
)

gcs_to_bigquery = GCSToBigQueryOperator(
    task_id="gcs_to_bigquery",
    bucket=bucket_name,
    source_objects=[processed_gcs_path],
    destination_project_dataset_table=big_query_table,
    write_disposition="WRITE_TRUNCATE", # truncates the table if it already exists
    skip_leading_rows=1,
    dag=dag,
    autodetect=True,
)


new_file_sensor >> trigger_spark_job >> move_file >> gcs_to_bigquery