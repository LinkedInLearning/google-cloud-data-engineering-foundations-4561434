import os
import json
from google.cloud import pubsub_v1
from dotenv import load_dotenv
from google.api_core.exceptions import AlreadyExists

os.environ.clear()
load_dotenv()


project_id = os.environ["GCP_PROJECT_ID"]
topic_name = os.environ["TOPIC_NAME"]
topic_name = f"projects/{project_id}/topics/{topic_name}"
service_account_path = os.environ["GCP_SERVICE_ACCOUNT_PATH"]

print(project_id, topic_name, service_account_path)

sample_data = {
    "Region": "Sub-Saharan Africa",
    "Country": "Chad",
    "ItemType": "OfficeSupplies",
    "SalesChannel": "Offline",
    "OrderPriority": "M",
    "OrderDate": "1/27/2011",
    "OrderID": "292494523",
    "ShipDate": "2/12/2011",
    "UnitsSold": 4484,
    "UnitPrice": 651.21,
    "UnitCost": 524.96,
}

publisher = pubsub_v1.PublisherClient.from_service_account_file(service_account_path)


def create_topic(topic_name):
    try:
        topic = publisher.create_topic(name=topic_name)
        print(f"Created topic: {topic.name}")
    except AlreadyExists:
        print(f"Topic {topic_name} already exists")
        return


def publish_message(data):
    if isinstance(data, str):
        bytes_data = data.encode("utf-8")
    else:
        bytes_data = json.dumps(sample_data).encode("utf-8")
    future = publisher.publish(topic_name, bytes_data)
    print(future.result())


if __name__ == "__main__":
    create_topic(topic_name)
    publish_message(sample_data)
    message = input("Enter any message to publish: (exit to quit)")
    while message != "exit":
        publish_message(message)
        message = input("Enter any message to publish: (exit to quit)")
