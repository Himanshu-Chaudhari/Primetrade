import requests
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '50',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b0825721-aa7d-4ea2-ac8e-84a8a2c65eaf',
}

try:
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status() 
    data = response.json()
    responseData = data['data']
    
    for i, currency in enumerate(responseData):
        name = currency['name']
        symbol = currency['symbol']
        price = currency['quote']['USD']['price']
        market_cap = currency['quote']['USD']['market_cap']
        volume_24h = currency['quote']['USD']['volume_24h']
        percent_change_24h = currency['quote']['USD']['percent_change_24h']
        
        print(f"{i+1}. Name: {name}")
        print(f"   Symbol: {symbol}")
        print(f"   Current Price (USD): ${price:,.2f}")
        print(f"   Market Capitalization: ${market_cap:,.2f}")
        print(f"   24-hour Trading Volume: ${volume_24h:,.2f}")
        print(f"   24-hour Price Change: {percent_change_24h:.2f}%\n")
        
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
