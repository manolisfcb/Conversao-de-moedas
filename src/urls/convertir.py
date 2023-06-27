from flask_restful import Resource
from flask import request
from controllers.getConversion import GetConversion
from resources.keycloak import login_required
from threading import Thread
from app import app
from flask_mail import Message
from app import mail

def enviar_correo(destinatario, asunto, cuerpo):
    
    mensaje = Message(asunto, recipients=[destinatario])
    mensaje.body = cuerpo
    mail.send(mensaje)

class Convertir(Resource):
    
    @login_required
    def get(self):
        try:
            """
            Parâmetros de saída:
            
                Moeda de origem: BRL
                Moeda de destino: USD
                Valor para conversão: R$ 5.000,00
                Forma de pagamento: Boleto
                Valor da "Moeda de destino" usado para conversão: $ 5,30
                Valor comprado em "Moeda de destino": $ 920,18 (taxas aplicadas no valor de compra diminuindo no valor total de conversão)
                Taxa de pagamento: R$ 72,50
                Taxa de conversão: R$ 50,00
                Valor utilizado para conversão descontando as taxas: R$ 4.877,50        
            """
            in_currency = request.json['in_currency']
            out_currency = request.json['out_currency']
            resp = GetConversion(in_currency, out_currency)

            amount = request.json['amount']
            payment_type = request.json['payment_type']
            resp.getConversion(amount, payment_type)
            respuesta = vars(resp)
            
            asunto = 'Conversão de moeda'
            cuerpo = 'Moeda de origem: ' + respuesta['Moeda_de_origem'] + '\n'

            Thread(target=enviar_correo, args=('mmedinac26gmail.com', asunto, cuerpo)).start()
            import time
            time.sleep(5)
            return respuesta
        except Exception as e:
            return {'message': str(e)}, 400