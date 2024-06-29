from airflow import DAG
from airflow.operators.python import PythonOperator
import random

from datetime import datetime

def print_hello():
    return "Hello world!"

def print_goodbye():
    return "Goodbye!"

def error_randomly():
    if random.choice([True, False]):
        raise ValueError("Error randomly")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "retries": 0,
}


dag = DAG(
    "demo_dag",
    default_args=default_args,
    description="Demo DAG",
    schedule=None,
)

hello_task = PythonOperator(
    task_id="hello_task",
    python_callable=print_hello,
    dag=dag,
)

goodbye_task = PythonOperator(
    task_id="goodbye_task",
    python_callable=print_goodbye,
    dag=dag,
)

error_task = PythonOperator(
    task_id="error_task",
    python_callable=error_randomly,
    dag=dag,
)


hello_task >> error_task >> goodbye_task
