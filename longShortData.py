import requests
import json

params = {
    "symbols": "BTCUSDT_PERP.A",
    "interval": "4hour",
    "from": 1678358400,  # UNIX timestamp for July 8, 2023, 00:00:00 UTC
    "to": 1678444799,  # UNIX timestamp for July 8, 2023, 23:59:59 UTC
    "api_key": "461e8931-6fc3-44a0-ad4f-ccb907ee0080"
}

url = "https://api.coinalyze.net/v1/long-short-ratio-history"

response = requests.get(url, params=params)

# Handle the response data as needed
data = response.json()

print(json.dumps(data, indent=2))
