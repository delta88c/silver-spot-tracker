import requests
from datetime import datetime

def get_silver_spot_price(api_key):
    url = f'https://metals-api.com/api/latest?access_key={api_key}&base=USD&symbols=XAG'
    r = requests.get(url)
    data = r.json()
    if 'error' in data:
        raise Exception(str(data['error']))
    price = data['rates']['XAG']
    timestamp = datetime.utcfromtimestamp(data['timestamp'])
    return price, timestamp
