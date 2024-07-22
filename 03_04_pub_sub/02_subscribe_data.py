import os
from google.cloud import pubsub_v1
from dotenv import load_dotenv
from google.api_core.exceptions import AlreadyExists

os.environ.clear()
load_dotenv()

project_id = os.environ["GCP_PROJECT_ID"]
topic_name = os.getenv("TOPIC_NAME")
subscriber_name = os.getenv("SUBSCRIPTION_NAME")

topic_name = f"projects/{project_id}/topics/{topic_name}"
subscription_path = f"projects/{project_id}/subscriptions/{subscriber_name}"
service_account_path = os.getenv("GCP_SERVICE_ACCOUNT_PATH")


subscriber = pubsub_v1.SubscriberClient.from_service_account_file(service_account_path)


def create_subscription():
    try:
        subscriber.create_subscription(name=subscription_path, topic=topic_name)
        print(f"Subscription created: {subscription_path}")
    except AlreadyExists:
        print(f"Subscription {subscription_path} already exists")
        return


def subscribe():
    # callback function that keeps listening
    def callback(message):
        print(f"Received message: {message}")
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)


if __name__ == "__main__":
    create_subscription()
    subscribe()
    print("Listening for messages on {}".format(subscription_path))
    while True:
        pass
