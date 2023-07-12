import requests
from tabulate import tabulate

# Define symbols and API parameters
symbols = """
    BTCUSDT_PERP.A, ETHUSDT_PERP.A, BNBUSDT_PERP.A, XRPUSDT_PERP.A, DOGEUSDT_PERP.A,
    SOLUSDT_PERP.A, LTCUSDT_PERP.A, MATICUSDT_PERP.A, AVAXUSDT_PERP.A, BCHUSDT_PERP.A,
    LINKUSDT_PERP.A, ATOMUSDT_PERP.A, LDOUSDT_PERP.A, ARBUSDT_PERP.A, AAVEUSDT_PERP.A,
    OPUSDT_PERP.A, MKRUSDT_PERP.A, APTUSDT_PERP.A
"""

convert_to_usd = "true"

currentUrl = "https://api.coinalyze.net/v1/open-interest"

params = {
    "symbols": symbols,
    "convert_to_usd": convert_to_usd,
    "api_key": "461e8931-6fc3-44a0-ad4f-ccb907ee0080"
}

# Send GET request
response = requests.get(currentUrl, params=params)

# Convert response to JSON
data = response.json()

# Sort the data in descending order based on open interest value
sorted_data = sorted(data, key=lambda x: x['value'], reverse=True)

# Prepare the data for tabulate
table_data = []
for item in sorted_data:
    symbol = item['symbol']
    oi_value = "{:.2f}".format(item['value'])  # Format value as a decimal with two decimal places
    table_data.append([symbol, oi_value])

# Display the data using tabulate
print(tabulate(table_data, headers=["Symbol", "Current Open Interest ($)"], tablefmt="psql", floatfmt=".2f"))


