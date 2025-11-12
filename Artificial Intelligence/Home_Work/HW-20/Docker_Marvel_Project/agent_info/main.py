import os
import json
import pika
import time
from openai import OpenAI

RABBIT_HOST = os.getenv("RABBIT_HOST", "rabbitmq")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def get_hero_info(hero_name: str):
    """Використовує OpenAI, щоб розповісти про героя."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": "Ти експерт по всесвіту Marvel. Розкажи все, що знаєш про вибраного героя (його історію, сили, ворогів)."},
                {"role": "user", "content": f"Розкажи мені про: {hero_name}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Не вдалося отримати інформацію: {e}"


def connect_rabbitmq():
    """Підключається до RabbitMQ."""
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST)
            )
            channel = connection.channel()
            return connection, channel
        except pika.exceptions.AMQPConnectionError:
            print("Очікування RabbitMQ...")
            time.sleep(3)


def main():
    connection, channel = connect_rabbitmq()

    channel.queue_declare(queue="hero_topic_queue")
    channel.queue_declare(queue="movie_request_queue")

    def callback(ch, method, properties, body):
        data = json.loads(body)
        hero = data['hero']
        print(f"🧠 Отримано завдання: розповісти про {hero}")

        info = get_hero_info(hero)

        print("=" * 40)
        print(f"ІНФОРМАЦІЯ ПРО: {hero.upper()}")
        print(info)
        print("=" * 40)

        message = {"hero": hero}
        channel.basic_publish(
            exchange="",
            routing_key="movie_request_queue",
            body=json.dumps(message)
        )
        print(f"Відправлено запит на фільми для {hero}...")

    print("🕵️‍♂️ Агент-Інфо очікує на героїв...")
    channel.basic_consume(queue="hero_topic_queue", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    main()
