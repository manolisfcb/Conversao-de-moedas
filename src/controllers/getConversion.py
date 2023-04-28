from service.awesomeapi import Awesomeapi
from resources.formaPagamento import FormaPagamento
class GetConversion:
    def __init__(self):
        self.response = []
    
    def convert_many(self, lista_currency, amount):
        Aweapi = Awesomeapi()
        conversão = Aweapi.convert_currency(lista_currency).response
        cambio = {}
        for conv in conversão:
            self.convertedAmount = float(conversão[conv]['bid']) * amount
            cambio['convertedAmount'] = self.convertedAmount
            cambio['Valor usado para conversão'] = conversão[conv]['bid']
            self.response.append(cambio)
        
        
        return self
    
    def total_a_pagar(self, convertedAmount, tipoPagamento):
  
        if tipoPagamento == 1:
            formaPagamento = FormaPagamento.pagamento_cartao_credito()
        else:
            formaPagamento = FormaPagamento.pagamento_boleto()
        total = 0

        for conv in [self.convertedAmount]:
            if conv < 3000:
                taxa_conversão = conv * 0.02
            else:
                taxa_conversão = conv * 0.01
            taxa_pagamento = conv * formaPagamento.taxa   
            total += conv - taxa_conversão - taxa_pagamento

        return {'total a pagar': total, 'taxa de conversão': taxa_conversão, 'taxa de pagamento': taxa_pagamento, 'forma de pagamento': formaPagamento.forma_de_pagamento.name}
    
    def getConversion(self, lista_currency, amount, tipoPagamento):
        
        self.convert_many(lista_currency, amount)
        
        self.total = self.total_a_pagar(self.convertedAmount, tipoPagamento)
        
        
        
        return self