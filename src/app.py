from flask import Flask, render_template
from flask_restful import Api
from service.awesomeapi import Awesomeapi
import requests
from urls.home import Home
from urls.convertir import Convertir
from urls.login import Login
from urls.logout import Logout
from urls.getStockinfo import GetStockinfo


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
api = Api(app)


@app.route('/get_all_combinations')
def hello_world():
    response = Awesomeapi()
    response.get_all_combinations()
    all_data = response.response
    return render_template('index.html', all_data=all_data)

api.add_resource(Home, '/')
api.add_resource(Convertir, '/convertir')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(GetStockinfo, '/getStockinfo')



if __name__ == '__main__':
    app.run(debug=True) # run our Flask app