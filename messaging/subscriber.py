import pika
import os
from dotenv import load_dotenv

load_dotenv()

# Read RabbitMQ connection info from .env
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
EXCHANGE_NAME = "sciot.topic"

def start_subscriber(routing_key: str, callback, queue_name: str = '', auto_ack: bool = True):
    """
    Start a RabbitMQ subscriber.
    
    :param routing_key: Topic routing key to bind to (e.g., "sensor.dht").
    :param callback: Function to handle incoming messages. Takes two args: channel and method, body.
    :param queue_name: Optional named queue (if empty, server auto-generates one).
    :param auto_ack: Whether to automatically acknowledge messages.
    """
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, 5672, '/', credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic', durable=True, auto_delete=False)

    # Create a queue (server-named if empty) and bind to exchange with the routing key
    result = channel.queue_declare(queue=queue_name, exclusive=(queue_name == ''), durable=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name, routing_key=routing_key)

    def wrapper(ch, method, properties, body):
        print(" Received from {}: {}".format(method.routing_key, body.decode()))
        callback(ch, method, body)

    channel.basic_consume(queue=queue_name, on_message_callback=wrapper, auto_ack=auto_ack)
    print(" [*] Waiting for messages with routing key '{}'. To exit press CTRL+C".format(routing_key))
    channel.start_consuming()
