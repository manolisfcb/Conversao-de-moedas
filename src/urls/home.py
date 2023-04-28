from flask_restful import Resource
from flask import render_template
from service.awesomeapi import Awesomeapi

class Home(Resource):
    def get(self):
        data = Awesomeapi().get_all_currencies_names().response
        return data