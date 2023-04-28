from flask_restful import Resource
import requests
from flask import request

class GetStockinfo(Resource):
    def get(self):
        stock = request.json['stock']
        
        response = requests.get(f'https://brapi.dev/api/available').json()
        print(len(response['stocks']))
        return response