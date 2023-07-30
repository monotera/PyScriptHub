from kafka import KafkaConsumer
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re

# Kafka server address
bootstrap_servers = "localhost:9092"

# Topic name
topic_name = "code_sender"

# Create Kafka consumer
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)


def run_function_from_string(function_string, *args):
    # Use regular expressions to find the function definition and extract the function name
    try:
        function_match = re.search(r"def\s+(\w+)\s*\(", function_string)
        if function_match:
            function_name = function_match.group(1)
        else:
            raise ValueError("Function definition not found in the string.")

        # Compile the function_string into a code object
        code_obj = compile(function_string, "<string>", "exec")

        # Create a new local namespace for the function
        local_namespace = {}

        # Execute the compiled code in the new namespace
        exec(code_obj, globals(), local_namespace)
        # Extract the function from the namespace
        if function_name in local_namespace:
            function = local_namespace[function_name]

            # Call the function with the provided arguments
            return function(*args)

        else:
            raise ValueError(f"Function '{function_name}' not found in the string.")
    except Exception as e:
        print(e)


# Function to consume and print messages from Kafka
def main():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    try:
        for message in consumer:
            function = message.value.decode("utf-8")
            print(function)
            run_function_from_string(function, driver)
    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        # Close the consumer to release resources
        consumer.close()


# Start consuming messages
if __name__ == "__main__":
    main()
