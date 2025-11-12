import pika
import json
import os
import time


RABBIT_HOST = os.getenv("RABBIT_HOST", "rabbitmq")


def connect_rabbitmq():
    """Спроба підключитися до RabbitMQ, доки не вдасться."""
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST)
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("Очікування RabbitMQ...")
            time.sleep(3)


def send_hero_topic(hero_name):
    """Відправляє ім'я героя першому агенту."""
    connection = connect_rabbitmq()
    channel = connection.channel()

    channel.queue_declare(queue="hero_topic_queue")

    message = {"hero": hero_name}
    channel.basic_publish(
        exchange="",
        routing_key="hero_topic_queue",
        body=json.dumps(message)
    )
    print(f"Відправлено запит на героя: {hero_name}")
    connection.close()


if __name__ == "__main__":
    while True:
        topic = input("Якого героя Marvel ви б хотіли обговорити? (або 'exit'): ")
        if topic.lower() == "exit":
            break
        send_hero_topic(topic)
