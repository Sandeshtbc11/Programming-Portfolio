"""
Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend.
"""

import requests  # For making HTTP requests
import sys  # For accessing command-line arguments

# Get the URL from the command-line argument
url = sys.argv[1]

try:
    # Send a GET request to the URL with a timeout of 5 seconds
    response = requests.get(url, timeout=5)

    # Check if the status code is 200 (OK)
    if response.status_code == 200:
        print(f"The website at {url} is working.")
    else:
        print(f"The website at {url} is not working. Status code: {response.status_code}")

except requests.RequestException:
    # Handle any exception that occurs during the request
    print(f"Could not connect to the website at {url}.")
