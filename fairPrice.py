import sys
import requests

# List of available symbols for the user to choose from
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "DOGEUSDT",
           "SOLUSDT", "LTCUSDT", "MATICUSDT", "AVAXUSDT", "BCHUSDT",
           "LINKUSDT", "ATOMUSDT", "LDOUSDT", "APTUSDT", "ARBUSDT",
           "OPUSDT", "MKRUSDT", "SNXUSDT", "AAVEUSDT", "NEARUSDT"]

print("Available Symbols:", symbols)

# Prompt the user to enter the symbol of the coin they want to view
symbol = input("Enter the symbol of the coin from the available symbols: ")

# Check if the entered symbol is valid
if symbol not in symbols:
    print("Invalid symbol. Please enter a valid symbol from the list.")
    sys.exit(1)

# Construct the API endpoint URL with the selected symbol
url = f"https://api-testnet.bybit.com/v5/market/orderbook?category=linear&symbol={symbol}"

payload = {}
headers = {}

try:
    # Make a GET request to the API endpoint
    response = requests.request("GET", url, headers=headers, data=payload)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    # Handle any errors that occur during the API request
    print("Error occurred:", e)
    sys.exit(1)

# Parse the response as JSON
data = response.json()

# Extract bid and ask data from the response
bid_data = [(float(bid[0]), float(bid[1])) for bid in data['result']['b']]
ask_data = [(float(ask[0]), float(ask[1])) for ask in data['result']['a']]

# Calculate total bid and ask sizes
total_bid_size = sum(size for _, size in bid_data)
total_ask_size = sum(size for _, size in ask_data)

# Calculate the weighted bid and ask prices
weighted_bid_price = sum(price * (size / total_bid_size) for price, size in bid_data)
weighted_ask_price = sum(price * (size / total_ask_size) for price, size in ask_data)

# Calculate the fair price as the average of weighted bid and ask prices
fair_price = (weighted_bid_price + weighted_ask_price) / 2

# Print bid prices and sizes
print("***BIDS***")
print("Bid Prices and Sizes:")
[print("Price:", price, "Size:", size) for price, size in bid_data]

# Print ask prices and sizes
print("***ASKS***")
print("Ask Prices and Sizes:")
[print("Price:", price, "Size:", size) for price, size in ask_data]

# Print the calculated weighted bid and ask prices
print("Weighted bid price:", weighted_bid_price)
print("Weighted ask price:", weighted_ask_price)

# Print the fair price
print("Fair Price:", fair_price)
