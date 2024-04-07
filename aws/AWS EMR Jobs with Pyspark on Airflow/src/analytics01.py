from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 7), 
    'email': ['goodwon593@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=10)
}

with DAG('airflow_for_emr_job_dag',
        default_args=default_args,
        # schedule_interval = '@weekly',
        catchup=False) as dag:

        # https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/empty/index.html#airflow.operators.empty.EmptyOperator
        start_pipeline = EmptyOperator(task_id="tsk_start_pipeline")

        start_pipeline
