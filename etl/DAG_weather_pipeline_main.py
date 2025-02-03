from datetime import datetime,timedelta
from airflow.models import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner":"Kemran",
    "retries":2,
    "depends_on_past":False,
    "start_date":datetime(2025,2,2,12),
    "retry_delay":timedelta(minutes=5)
}

dag_args1=DAG("main-etl","load current weather",
              default_args=default_args,
              schedule='0 3 * * *',
              max_active_tasks=1,
              max_active_runs=1,
              tags=["etl","d_weather","d_cities"])

start_main = BashOperator(
    task_id="start_main",
    bash_command='source /py_envs/bin/activate && python /airflow/scripts/Weather_data_pipeline/main.py',
    dag=dag_args1
)



