import requests

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
    
    sorted_data = sorted(responseData, key=lambda x: x['quote']['USD']['market_cap'], reverse=True)
    
    top_5 = sorted_data[:5]

    max_change = -float('inf')
    min_change = float('inf')
    max_currency = None
    min_currency = None
    
    print("Top 5 Cryptocurrencies by Market Capitalization:\n")
    for i, currency in enumerate(top_5):
        name = currency['name']
        symbol = currency['symbol']
        price = currency['quote']['USD']['price']
        market_cap = currency['quote']['USD']['market_cap']
        volume_24h = currency['quote']['USD']['volume_24h']
        percent_change_24h = currency['quote']['USD']['percent_change_24h']

        if percent_change_24h > max_change:
            max_change = percent_change_24h
            max_currency = (name, symbol, max_change)
        
        if percent_change_24h < min_change:
            min_change = percent_change_24h
            min_currency = (name, symbol, min_change)

    print(f"The cryptocurrency with the highest 24-hour percentage price change:")
    print(f"Name: {max_currency[0]}, Symbol: {max_currency[1]}, Change: {max_currency[2]:.2f}%\n")
    
    print(f"The cryptocurrency with the lowest 24-hour percentage price change:")
    print(f"Name: {min_currency[0]}, Symbol: {min_currency[1]}, Change: {min_currency[2]:.2f}%")

        
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")

total_price = sum(currency['quote']['USD']['price'] for currency in responseData)
average_price = total_price/50
print(f"The average price of the top 50 cryptocurrencies is: ${average_price:,.2f}")