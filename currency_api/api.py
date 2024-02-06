import requests

def get_api():
    url = 'https://v6.exchangerate-api.com/v6/1951c2b25327862821adc02d/latest/USD'
    response = requests.get(url)
    data = response.json()
    conversion_rates = data['conversion_rates']
    euros = (conversion_rates['EUR'])
    return euros

