from pybit.unified_trading import HTTP
import requests

url = "https://api-testnet.bybit.com/v5/market/orderbook?category=linear&symbol=BTCUSDT"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
