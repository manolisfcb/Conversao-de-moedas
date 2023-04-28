from flask_restful import Resource
from flask import request
from controllers.getConversion import GetConversion

class Convertir(Resource):
    def get(self):
        in_currency = request.json['in_currency']
        out_currency = request.json['out_currency']
        lista_currency = [in_currency +'-'+out_currency]
        amount = request.json['amount']
        payment_type = request.json['payment_type']
        resp = GetConversion().getConversion(lista_currency, amount, payment_type)

        
        return resp