# Apache Airflow on Cloud Composer

Apache Airflow is a platform to programmatically author, schedule and monitor workflows. 
It can be use to tie down pipelines across all the tools we have seen so far.

## Composer

Cloud Composer is a managed workflow automation tool that is built on Apache Airflow. Since Airflow's infrastructure is quite complex managing them can become a nightmare
Cloud Composer is a managed service that abstracts away the complexity of managing the infrastructure.

## Cloud Console

1. Go to the Cloud Composer page in the Cloud Console.
2. Click Create Environment. You can select composer version 2, since the Version 3 is in beta.
3. Enter a name, select a location and select the machine type.
4. For the sake of hobby project you can select the smallest machine type, but for production you might want to choose on based on your project
5. Leave every other setting as default and click Create.

Note:: Creation will take sometime so don't worry!

## Composer Items

1. The environment variables
2. The Python packages
3. The DAG storage
4. The Airflow configuration
5. Logs

## Airflow UI

Unlike DataProc or Dataflow, Apache airflow has a UI that you can access to monitor your workflows. 
You can access the UI by clicking on the environment you created and clicking on the Airflow Webserver link.

Learning Airflow UI in itself can be quite a task, Explore the following pages as shown in the video.

1. The list of dags
2. The dag page 
3. The graph view
4. The tree view
5. Running a dag
6. Checking the logs
7. Connections
8. Variables

## DAGs Development

1. We have two types of dags in this project one is a simple dag for your to understand what a dag is and how to run it
2. The sales data processor ties down all the tools we have seen so far.

Upload both to your airflow GCS bucket
It will show up on the airflow UI after a few minutes.
Run them and see the results. 

