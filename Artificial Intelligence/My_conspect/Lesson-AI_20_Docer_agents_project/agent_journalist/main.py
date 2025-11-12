import os
import json
import pika
import time
from openai import OpenAI

RABBIT_HOST = os.getenv("RABBIT_HOST", "rabbitmq")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_news(topic: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Ти журналіст, який пише короткі новини українською."},
            {"role": "user", "content": f"Напиши коротку новину на тему: {topic}"}
        ]
    )
    return response.choices[0].message.content.strip()


def connect_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
            channel = connection.channel()
            return connection, channel
        except pika.exceptions.AMQPConnectionError:
            print("Очікування RabbitMQ...")
            time.sleep(3)


def main():
    connection, channel = connect_rabbitmq()
    channel.queue_declare(queue="topics")
    channel.queue_declare(queue="news_raw")

    def on_topic(ch, method, properties, body):
        data = json.loads(body)
        topic = data["topic"]
        print(f"Отримано тему: {topic}")
        news = generate_news(topic)
        message = {"topic": topic, "text": news}
        channel.basic_publish(exchange="", routing_key="news_raw", body=json.dumps(message))
        print("Новину відправлено до редактора!")

    print("Журналіст очікує тем...")
    channel.basic_consume(queue="topics", on_message_callback=on_topic, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    main()
