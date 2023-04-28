import requests
def hello_world():
    resp = requests.get('https://economia.awesomeapi.com.br/json/available')
    print(resp)
    return resp

#resp = hello_world()

def convert_currency(list_of_currencies):
    
    url = f'https://economia.awesomeapi.com.br/last/'
    for currency in list_of_currencies:
        url += currency + ','
        
    print(url)
    req = requests.get(url).json()
    
    return req

list_of_currencies = ['USD-BRL','EUR-BRL','BTC-BRL']

resp = convert_currency(list_of_currencies)

