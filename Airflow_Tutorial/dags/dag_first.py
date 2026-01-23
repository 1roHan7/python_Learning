from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='dag_ELTpipeline_v1',
    default_args=default_args,
    description='My first DAG',
    start_date= datetime(2025, 7, 17,2),
    schedule='@daily'
) as dag:
    mini_ETL_v1 = BashOperator(
        task_id = 'ETL_mini_project',
        bash_command = 'python3 /opt/airflow/mini_ETL_project/main.py'
    )

    mini_ETL_v1
