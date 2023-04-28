import requests

class Awesomeapi:
    
    def __init__(self):
        self._url = 'https://economia.awesomeapi.com.br/json/'
        self.response = None

    def get_all_combinations(self):
        url_request = self._url+'available'
        self.response = requests.get(url_request).json()
        return self

    def get_all_currencies_names(self):
        url_request = self._url+'available/uniq'
        self.response = requests.get(url_request).json()
        return self
    
    def convert_currency(self,list_of_currencies):
        
        url = f'https://economia.awesomeapi.com.br/last/{list_of_currencies[0]}'
        self.response = requests.get(url).json()
       
        return self