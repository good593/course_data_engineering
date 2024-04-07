from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.empty import EmptyOperator
import boto3
from airflow.providers.amazon.aws.operators.emr import (
    EmrCreateJobFlowOperator, 
    EmrAddStepsOperator,
    EmrTerminateJobFlowOperator)
from airflow.providers.amazon.aws.sensors.emr import EmrJobFlowSensor, EmrStepSensor

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

job_flow_overrides = {
    "Name": "airflow_emr_cluster",
    "ReleaseLabel": "emr-6.13.0",
    "Applications": [{"Name": "Spark"}, {"Name": "JupyterEnterpriseGateway"}],
    "LogUri": "s3://course-good593/airflow/logs/", # 생성한 S3 폴더 
    "VisibleToAllUsers":False,
    "Instances": {
        "InstanceGroups": [
            {
                "Name": "Master node",
                "Market": "ON_DEMAND",
                "InstanceRole": "MASTER",
                "InstanceType": "m5.xlarge",
                "InstanceCount": 1,
            },
            {
                "Name": "Core node",
                "Market": "ON_DEMAND", # Spot instances are a "use as available" instances
                "InstanceRole": "CORE",
                "InstanceType": "m5.xlarge",
                "InstanceCount": 1,
            },
        ],
         
        "Ec2SubnetId": "subnet-088bb3a6999d356a3", # 생성한 VPC subnet id
        "Ec2KeyName" : 'emr-keypair-airflow', # 생성한 key pair
        "KeepJobFlowAliveWhenNoSteps": True,
        "TerminationProtected": False, # Setting this as false will allow us to programmatically terminate the cluster
    },
    # 생성한 EMR Role
    "JobFlowRole": "EMR_EC2_DefaultRole",
    "ServiceRole": "EMR_DefaultRole",
   
}

with DAG('airflow_for_emr_job_dag',
        default_args=default_args,
        # schedule_interval = '@weekly',
        catchup=False) as dag:

        start_pipeline = EmptyOperator(task_id="tsk_start_pipeline")

        # Create an EMR cluster
        create_emr_cluster = EmrCreateJobFlowOperator(
            task_id="tsk_create_emr_cluster",
            job_flow_overrides=job_flow_overrides,
            # aws_conn_id="aws_default",
            # emr_conn_id="emr_default",
        )

        is_emr_cluster_created = EmrJobFlowSensor(
        task_id="tsk_is_emr_cluster_created", 
        job_flow_id="{{ task_instance.xcom_pull(task_ids='tsk_create_emr_cluster', key='return_value') }}",
        target_states={"WAITING"},  # Specify the desired state
        timeout=3600,
        poke_interval=5,
        mode='poke',
        )

        remove_cluster = EmrTerminateJobFlowOperator(
        task_id="tsk_remove_cluster",
        job_flow_id="{{ task_instance.xcom_pull(task_ids='tsk_create_emr_cluster', key='return_value') }}",
        )

        is_emr_cluster_terminated = EmrJobFlowSensor(
        task_id="tsk_is_emr_cluster_terminated", 
        job_flow_id="{{ task_instance.xcom_pull(task_ids='tsk_create_emr_cluster', key='return_value') }}",
        target_states={"TERMINATED"},  # Specify the desired state
        timeout=3600,
        poke_interval=5,
        mode='poke',
        )

        end_pipeline = EmptyOperator(task_id="tsk_end_pipeline")

        start_pipeline >> create_emr_cluster >> is_emr_cluster_created >> remove_cluster >> is_emr_cluster_terminated >> end_pipeline


