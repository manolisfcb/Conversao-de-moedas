from flask import Flask, render_template
from flask_restful import Api
from service.awesomeapi import Awesomeapi
import requests

from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Configura el servidor SMTP que usarás
app.config['MAIL_PORT'] = 587  # Configura el puerto del servidor SMTP
app.config['MAIL_USE_TLS'] = True  # Configura el uso de TLS
app.config['MAIL_USERNAME'] = 'mmedinac26@gmail.com'  # Configura tu dirección de correo electrónico
app.config['MAIL_PASSWORD'] = 'a+320Copiloto'  # Configura la contraseña de tu correo electrónico
app.config['MAIL_DEBUG'] = 0
mail = Mail(app)
app.config.from_object('config.DevelopmentConfig')
api = Api(app)

@app.route('/enviar-correo')
def enviar_correo():
    msg = Message('Asunto del correo', sender='mmedinac26@gmail.com', recipients=['mmedinac26@gmail.com'])
    msg.body = "Contenido del correo"

    with app.app_context():
        mail.send(msg)

    return 'Correo enviado'


@app.route('/get_all_combinations')
def hello_world():
    response = Awesomeapi()
    response.get_all_combinations()
    all_data = response.response
    return render_template('login.html')
from urls.home import Home
from urls.convertir import Convertir
from urls.login import Login
from urls.logout import Logout
from urls.getStockinfo import GetStockinfo
api.add_resource(Home, '/')
api.add_resource(Convertir, '/convertir')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(GetStockinfo, '/getStockinfo')



if __name__ == '__main__':
    app.run(debug=True) # run our Flask app