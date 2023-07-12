import datetime
import time
import requests
from tabulate import tabulate

# Get current time and calculate timestamp for 24 hours ago
current_time = int(time.time())
twenty_four_hours_ago = current_time - 24*60*60

# Define symbols and API parameters
symbols = ["BTCUSDT_PERP.A", "ETHUSDT_PERP.A", "BNBUSDT_PERP.A", "XRPUSDT_PERP.A", "DOGEUSDT_PERP.A",
           "SOLUSDT_PERP.A", "LTCUSDT_PERP.A", "MATICUSDT_PERP.A", "AVAXUSDT_PERP.A", "BCHUSDT_PERP.A",
           "LINKUSDT_PERP.A", "ATOMUSDT_PERP.A", "LDOUSDT_PERP.A", "APTUSDT_PERP.A", "ARBUSDT_PERP.A",
           "OPUSDT_PERP.A", "MKRUSDT_PERP.A", "SNXUSDT_PERP.A", "AAVEUSDT_PERP.A", "NEARUSDT_PERP.A"]

params = {
    "symbols": symbols[9],  # Change the index as needed to select the desired symbol
    "interval": "6hour",
    "from": twenty_four_hours_ago,
    "to": current_time,
    "api_key": "461e8931-6fc3-44a0-ad4f-ccb907ee0080"
}

url = "https://api.coinalyze.net/v1/long-short-ratio-history"

try:
    # Make the API request and handle potential errors
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    # Parse the response JSON data
    data = response.json()

    formatted_data = []

    # Process the data and format the timestamp
    for entry in data[0].get('history', []):
        timestamp = entry.get('t')
        if timestamp is not None:
            formatted_timestamp = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            formatted_entry = {
                'symbol': params['symbols'],
                'timestamp': formatted_timestamp,
                'ratio': entry.get('r'),
                'long_percentage': entry.get('l'),
                'short_percentage': entry.get('s')
            }
            formatted_data.append(formatted_entry)

    # Print the formatted data
    print(tabulate(formatted_data, headers="keys", tablefmt="psql"))


except requests.exceptions.RequestException as e:
    print("Error making the API request:", str(e))
