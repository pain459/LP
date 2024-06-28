from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_from_source():
    source_pg_hook = PostgresHook(postgres_conn_id='source_postgres')
    records = source_pg_hook.get_records(sql="SELECT * FROM your_table")
    return records

def transform(records):
    # Apply any transformation logic
    transformed_records = [record for record in records]
    return transformed_records

def load_to_warehouse(records):
    warehouse_pg_hook = PostgresHook(postgres_conn_id='warehouse_postgres')
    for record in records:
        warehouse_pg_hook.run(sql="INSERT INTO your_warehouse_table VALUES (%s, %s, %s)", parameters=record)

with DAG('etl_pipeline', default_args=default_args, schedule_interval='@daily', start_date=datetime(2023, 1, 1)) as dag:
    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_from_source
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_to_warehouse
    )

    extract >> transform >> load
