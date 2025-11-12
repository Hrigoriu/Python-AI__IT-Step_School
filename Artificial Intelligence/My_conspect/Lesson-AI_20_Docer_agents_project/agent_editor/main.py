import os
import json
import pika
import time
from openai import OpenAI

RABBIT_HOST = os.getenv("RABBIT_HOST", "rabbitmq")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def edit_text(text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Ти професійний редактор українських текстів."},
            {"role": "user", "content": f"Відредагуй цей текст:\n{text}"}
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


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Отримано новину на тему: {data['topic']}")
    edited = edit_text(data["text"])
    print("Відредагований текст:")
    print("=" * 40)
    print(edited)
    print("=" * 40)


def main():
    connection, channel = connect_rabbitmq()
    channel.queue_declare(queue="news_raw")
    channel.basic_consume(queue="news_raw", on_message_callback=callback, auto_ack=True)

    print("🕵️‍♂️ Редактор очікує повідомлень...")
    channel.start_consuming()


if __name__ == "__main__":
    main()
