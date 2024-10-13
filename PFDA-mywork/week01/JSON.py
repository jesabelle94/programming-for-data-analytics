# Write a program to print this JSON to the console
# Author: Jenny Formentera

import requests

# Define the URL
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# Send a GET request to the URL
response = requests.get(url)

data = response.json()
# Print the JSON data

print(data)
