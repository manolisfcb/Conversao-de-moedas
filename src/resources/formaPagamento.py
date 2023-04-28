from enum import Enum

class Pagamento(Enum):
    CARTAO_CRED = 1
    BOLETO = 2

class FormaPagamento:
    
    def __init__(self, forma_de_pagamento, taxa):
        self.forma_de_pagamento = forma_de_pagamento
        self.taxa = taxa

    @staticmethod
    def pagamento_cartao_credito():
        return FormaPagamento(Pagamento.CARTAO_CRED, 0.0763)
    
    @staticmethod
    def pagamento_boleto():
        return FormaPagamento(Pagamento.BOLETO, 0.0145)
            
            
