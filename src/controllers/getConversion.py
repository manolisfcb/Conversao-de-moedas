from service.awesomeapi import Awesomeapi
from resources.formaPagamento import FormaPagamento
class GetConversion:
    def __init__(self, currency_in, currency_out):
        self.Moeda_de_origem = currency_in
        self.Moeda_de_destino = currency_out
    
    
    def get_taxa_de_conversao(self):
        Aweapi = Awesomeapi()
        par_moedas = [self.Moeda_de_origem +'-'+self.Moeda_de_destino]
        conversão = Aweapi.convert_currency(par_moedas).response
        for conv in conversão:
            self.taxa_conversão = conversão[conv]['bid']
        return self
    
    def get_valor_comprado(self, amount):
        self.valor_comprado = float(self.taxa_conversão) * amount
        return self
    
    
    def total_a_pagar(self, tipoPagamento, amount):
  
        if tipoPagamento == 'CARTAO_CRED':
            formaPagamento = FormaPagamento.pagamento_cartao_credito()
        elif tipoPagamento == 'BOLETO':
            formaPagamento = FormaPagamento.pagamento_boleto()
        else:
            raise Exception('Forma de pagamento não encontrada')
        
        
        total = 0

        for conv in [amount]:
            if conv < 3000:
                taxa_conversão = conv * 0.02
            else:
                taxa_conversão = conv * 0.01
            taxa_pagamento = conv * formaPagamento.taxa   
            total += conv - taxa_conversão - taxa_pagamento

        self.total = total
        self.taxa_conversão = taxa_conversão
        self.taxa_pagamento = taxa_pagamento
        self.formaPagamento = formaPagamento.forma_de_pagamento.name
        return self
    
    def getConversion(self, amount, tipoPagamento):

        
        self.total_a_pagar(tipoPagamento, amount)
        
        return self
        
    
    def get_response(self):
        return vars(self)