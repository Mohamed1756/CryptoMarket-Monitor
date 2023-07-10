import requests

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

# Display current open interest for each symbol in separate columns
print("Symbol\t\t\tCurrent Open Interest ($) ")
print("----------------------------------------")
for item in sorted_data:
    symbol = item['symbol']
    oi_value = round(item['value'], 2)
    print(f"{symbol}\t{oi_value}")
