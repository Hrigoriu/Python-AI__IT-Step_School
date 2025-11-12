import pika, json, os

RABBIT_HOST = os.getenv("RABBIT_HOST", "rabbitmq")


def send_topic(topic):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
    channel = connection.channel()
    channel.queue_declare(queue="topics")
    message = {"topic": topic}
    channel.basic_publish(exchange="", routing_key="topics", body=json.dumps(message))
    print(f"Відправлено тему: {topic}")
    connection.close()


if __name__ == "__main__":
    while True:
        topic = input("Введіть тему новини (або 'exit'): ")
        if topic.lower() == "exit":
            break
        send_topic(topic)
