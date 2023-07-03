from pybit.unified_trading import HTTP
import requests
import json

url = "https://api-testnet.bybit.com/v5/market/orderbook?category=linear&symbol=BTCUSDT"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# Parse the response as JSON
data = json.loads(response.text)

# Extract the bid and ask prices and sizes
bid_data = [(float(bid[0]), float(bid[1])) for bid in data['result']['b']]
ask_data = [(float(ask[0]), float(ask[1])) for ask in data['result']['a']]

# Extract bid prices and ask prices separately
bid_prices = [bid[0] for bid in bid_data]
ask_prices = [ask[0] for ask in ask_data]

# Calculate the fair price
fair_price = (max(bid_prices) + min(ask_prices)) / 2

print("***BIDS***")
print("Bid Prices and Sizes:")
for price, size in bid_data:
    print("Price:", price, "Size:", size)

print("***ASKS***")
print("Ask Prices and Sizes:")
for price, size in ask_data:
    print("Price:", price, "Size:", size)

print("Fair Price:", fair_price)
