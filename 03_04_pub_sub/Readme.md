# Cloud Pub/Sub

Cloud Pub/Sub is a messaging service that allows you to send and receive messages between independent applications. It is a fully managed service that scales automatically based on the volume of messages. It is a global service that allows you to send messages between applications running in different regions.

## Setup

1. Go to google cloud console
2. Create a pub/sub topic
3. Create a subscription
4. Copy the ID/Name of the topic and subscription into the env file
5. Ensure you have the service account JSON downlaoded and inside the repo

## Setup

The repo already installs the required libraries. If you are running this on your local machine, you can install the required libraries using the following command

```
pip install google-cloud-pubsub python-dotenv
```

## Running the code

You need to run the publisher and subscriber code in two different terminals.

### Publisher

```
python publish_data.py
```

### Subscriber

```
python subscribe_data.py
```