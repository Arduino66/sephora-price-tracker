from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("Hello Airflow!")

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    'hello_airflow',
    schedule_interval=None,  # No automatic scheduling
    catchup=False,
    default_args=default_args,
    tags=['test'],
) as dag:
    
    hello_task = PythonOperator(
        task_id='say_hello',
        python_callable=say_hello
    )
