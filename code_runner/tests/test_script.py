from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re


def run_function_from_string(function_string, *args):
    # Use regular expressions to find the function definition and extract the function name
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


# Example usage:
function_string = """
def init_driver(driver, url):
    raw_html = driver.get(url)
    raw_html = driver.page_source
    return driver
"""

function_string_2 = """
def search_google(driver, query):
    search_box = driver.find_element(By.NAME, 'q')
    search_query = query
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    return driver
"""


def main():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()

    i = 0
    # In the future this will be true
    while i < 5:
        url = "https://www.google.com/"
        if i == 0:
            driver = run_function_from_string(function_string, driver, url)
        elif i == 1:
            driver = run_function_from_string(function_string_2, driver, "Hello world!")
        else:
            print("Testing if selenium is active")

        time.sleep(2)
        i += 1


if __name__ == "__main__":
    main()
