from kafka import KafkaProducer
import time
from openai_utils import get_code_from_open_ai
import re
import pprint

# Kafka server address
bootstrap_servers = "localhost:9092"

# Topic name
topic_name = "code_sender"

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)


def send_message(message):
    producer.send(topic_name, value=message.encode("utf-8"))
    producer.flush()


def main():
    history_messages = []
    while True:
        action = input("Enter a web action or exit to quit: ")
        if action.lower() == "exit":
            producer.close()
            break
        is_error = input("Is this an error? (y/n): ")
        is_error = is_error.lower() == "y"
        history_messages, message = get_code_from_open_ai(
            action, history_messages, is_error
        )
        pprint.pprint(history_messages)
        send_message(message)
        print(f"Message '{message}' sent to Kafka.")


if __name__ == "__main__":
    main()
