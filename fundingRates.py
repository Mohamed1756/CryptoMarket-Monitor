import requests
import datetime
from tabulate import tabulate

symbols = """
    BTCUSDT_PERP.A, ETHUSDT_PERP.A, BNBUSDT_PERP.A, XRPUSDT_PERP.A, DOGEUSDT_PERP.A,
    SOLUSDT_PERP.A, LTCUSDT_PERP.A, MATICUSDT_PERP.A, AVAXUSDT_PERP.A, BCHUSDT_PERP.A,
    LINKUSDT_PERP.A, ATOMUSDT_PERP.A, LDOUSDT_PERP.A, ARBUSDT_PERP.A, AAVEUSDT_PERP.A,
    OPUSDT_PERP.A, MKRUSDT_PERP.A, APTUSDT_PERP.A
"""

urlFR = "https://api.coinalyze.net/v1/funding-rate"
urlPFR = "https://api.coinalyze.net/v1/predicted-funding-rate"

params = {
    "symbols": symbols,
    "api_key": "461e8931-6fc3-44a0-ad4f-ccb907ee0080"
}

# Send GET request for Funding Rate
responseFR = requests.get(urlFR, params=params)

# Send GET request for Predicted Funding Rate
responsePFR = requests.get(urlPFR, params=params)

# Convert responses to JSON
dataFR = responseFR.json()
dataPFR = responsePFR.json()

# Convert UNIX timestamp to readable timestamp
formatted_dataFR = []
for entry in dataFR:
    symbol = entry['symbol']
    fr_value = entry['value']
    timestamp = datetime.datetime.fromtimestamp(entry['update'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
    formatted_entry = {
        'Symbol': symbol,
        'Funding Rate': fr_value,
        'Timestamp': timestamp
    }
    formatted_dataFR.append(formatted_entry)

formatted_dataPFR = []
for entry in dataPFR:
    symbol = entry['symbol']
    pfr_value = entry['value']
    timestamp = datetime.datetime.fromtimestamp(entry['update'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
    formatted_entry = {
        'Symbol': symbol,
        'Predicted Funding Rate': pfr_value,
        'Timestamp': timestamp
    }
    formatted_dataPFR.append(formatted_entry)

# Merge Funding Rate and Predicted Funding Rate data
combined_data = []
for fr_entry in formatted_dataFR:
    symbol = fr_entry['Symbol']
    fr_value = fr_entry['Funding Rate']
    timestamp = fr_entry['Timestamp']
    pfr_entry = next((entry for entry in formatted_dataPFR if entry['Symbol'] == symbol), None)
    pfr_value = pfr_entry['Predicted Funding Rate'] if pfr_entry else None
    combined_entry = {
        'Symbol': symbol,
        'Funding Rate': fr_value,
        'Predicted Funding Rate': pfr_value,
        'Timestamp': timestamp
    }
    combined_data.append(combined_entry)

# Sort the combined data based on 'Funding Rate' in ascending order
combined_data.sort(key=lambda x: x['Funding Rate'])

# Print the combined data in columns
print("Funding Rate and Predicted Funding Rate Data:")
print(tabulate(combined_data, headers="keys", tablefmt="psql"))


