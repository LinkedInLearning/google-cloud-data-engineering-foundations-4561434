# Google Cloud Storage

Google Cloud Storage is an infinite closet to store of all forms of data. From the video, you would have already seen how to create a bucket and upload files to it. Use the guidlines here upload files using Python script and Cloud SDK.

## Creating a service account

1. Go to the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page in the Google Cloud Console.
2. Click on the `Create Service Account` button.
3. Enter a name for the service account and click on the `Create` button.
4. Select the role for the service account as storage admin and click on the `Continue` button.
5. Click on the `Done` button.


## Uploading files using Python script

1. Install the Google Cloud Storage library for Python using the following command:

```bash
pip install google-cloud-storage
```

2. Now let's use the python script to upload files to the bucket. Create a new python file and copy the following code:

3. Run the script using the following command:

```bash
python gcs_script.py
```

## Uploading files using Cloud SDK
