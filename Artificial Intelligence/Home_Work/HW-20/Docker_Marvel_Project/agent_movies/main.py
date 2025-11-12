import os
import json
import pika
import time
from openai import OpenAI

# Налаштування змінних середовища
RABBIT_HOST = os.getenv("RABBIT_HOST", "rabbitmq")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ініціалізація клієнта OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)


def get_hero_movies(hero_name: str) -> str:
    """Використовує OpenAI, щоб знайти фільми або мультфільми з героєм Marvel."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ти кінокритик і експерт Marvel. "
                        "Назви фільми або мультфільми, де з'являється цей герой."
                    ),
                },
                {"role": "user", "content": f"Фільми та мультфільми з героєм: {hero_name}"},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Не вдалося отримати список фільмів: {e}"


def connect_rabbitmq():
    """Спроба підключитися до RabbitMQ, доки не вдасться."""
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST)
            )
            channel = connection.channel()
            return connection, channel
        except pika.exceptions.AMQPConnectionError:
            print("🐇 Очікування RabbitMQ...")
            time.sleep(3)


def main():
    connection, channel = connect_rabbitmq()

    # Декларуємо чергу для отримання запитів
    channel.queue_declare(queue="movie_request_queue")

    # Обробник повідомлень із черги
    def callback(ch, method, properties, body):
        data = json.loads(body)
        hero = data["hero"]
        print(f"🎬 Отримано завдання: знайти фільми для {hero}")

        movies = get_hero_movies(hero)

        print("=" * 40)
        print(f"ФІЛЬМИ З ГЕРОЄМ: {hero.upper()}")
        print(movies)
        print("=" * 40)

    print("🍿 Агент-Кіноман очікує на героїв...")
    channel.basic_consume(
        queue="movie_request_queue",
        on_message_callback=callback,
        auto_ack=True,
    )

    channel.start_consuming()


if __name__ == "__main__":
    main()
