# Google Cloud DataProc

DataProc is a managed service for running Apache Spark clusters. In this folder, we have two apache spark jobs that are run on Google Cloud DataProc. 

1. The first job does some basic analysis on sales data. It's similar to pandas dataframe
2. The 2nd job splits the sales file based on online and offline sales and saves the output in separate files.

## Running the script

1. Upload the script to a google cloud storage bucket.
2. You can go to the google cloud console, create a new job on the cluster and run the script by providing the path to the script in the bucket.

## Install and Authenticate GCloud CLI

Follow the instructions here
https://cloud.google.com/sdk/docs/install

## Running from Local

Often times you might want to make changes in the local and test it in dataproc. Uploading the script to the bucket every time is not efficient. You can use the `gcloud` command to run the script from the local.

```bash
gcloud dataproc jobs submit pyspark 03_03_dataproc/03_split_data.py  --cluster=cluster-11fc --region us-central1
```
You can see the job running right there on your console.