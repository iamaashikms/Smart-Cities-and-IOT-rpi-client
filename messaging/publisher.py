import pika
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Read RabbitMQ connection info from .env
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
EXCHANGE_NAME = "sciot.topic"

# Set up RabbitMQ connection
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, 5672, '/', credentials))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic', durable=True, auto_delete=False)

def publish_message(routing_key: str, message):
    """Publish message to RabbitMQ topic exchange. Accepts dict or str."""

    if isinstance(message, dict):
        # Convert dictionary to JSON string
        message = json.dumps(message)

    if not isinstance(message, str):
        raise TypeError("Message must be a string or dict.")

    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=routing_key, body=message)
    print("Sent to '{}': {}".format(routing_key, message))
