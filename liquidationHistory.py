import datetime
import time
import requests
from tabulate import tabulate

# Get current time and calculate timestamp for 24 hours ago
current_time = int(time.time())
twenty_four_hours_ago = current_time - 24 * 60 * 60

# Define symbols and API parameters
symbols = ["BTCUSDT_PERP.A", "ETHUSDT_PERP.A", "BNBUSDT_PERP.A", "XRPUSDT_PERP.A", "DOGEUSDT_PERP.A",
           "SOLUSDT_PERP.A", "LTCUSDT_PERP.A", "MATICUSDT_PERP.A", "AVAXUSDT_PERP.A", "BCHUSDT_PERP.A",
           "LINKUSDT_PERP.A", "ATOMUSDT_PERP.A", "LDOUSDT_PERP.A", "APTUSDT_PERP.A", "ARBUSDT_PERP.A",
           "OPUSDT_PERP.A", "MKRUSDT_PERP.A", "SNXUSDT_PERP.A", "AAVEUSDT_PERP.A", "NEARUSDT_PERP.A"]

url = "https://api.coinalyze.net/v1/liquidation-history"

# Fetch liquidation history for each symbol
params = {
    "symbols": symbols[5],  # Change the index as needed to select the desired symbol
    "interval": "12hour",  # change Timeframe
    "from": twenty_four_hours_ago,
    "to": current_time,
    "api_key": "461e8931-6fc3-44a0-ad4f-ccb907ee0080",
    "convert_to_usd": "true"
}

# Send GET request
response = requests.get(url, params=params)

# Convert response to JSON
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
            'Long liquidations': entry.get('l'),
            'Short Liquidations': entry.get('s'),
            'Total liquidations ($)': round(entry.get('l') + entry.get('s'), 2)
        }
        formatted_data.append(formatted_entry)

# Print the combined data in columns
print("Liquidation History")
print(tabulate(formatted_data, headers="keys", tablefmt="psql"))
