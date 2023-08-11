#!/usr/bin/python3
import requests

# Set up the API endpoint and parameters
api_url = "https://api.datadoghq.com/api/v1/dashboard/"
api_key = "47a9d94addecd780b76cd27d04375e03"
api_app_key = "36bdaae8e1bd824d5c38c6d07ea7a7ac31c13557"
headers = {'Content-type': 'application/json', 'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': api_app_key}
query_params = {'filter': 'host:221107-web-01'}

# Make the API call to get the host details
response = requests.get(api_url, headers=headers, params=query_params)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    print(response_json)
