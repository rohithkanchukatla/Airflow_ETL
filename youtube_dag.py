from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from python_script import process_comments

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 29),  # Fixed incorrect date format
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'youtube_dag',
    default_args=default_args,
    description='Youtube ETL DAG',
    schedule_interval=timedelta(days=1)  # Set your desired schedule interval
)

run_etl = PythonOperator(
    task_id='youtube_ETL',
    python_callable=process_comments,
    dag=dag
)

run_etl
