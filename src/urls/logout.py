from flask_restful import Resource
from resources.keycloak import *
from flask import make_response,session, jsonify

class Logout(Resource):
    
    def get(self):
        response = make_response(jsonify({'message': 'Logout realizado com sucesso'}))
        response.set_cookie('access_token', '', expires=0)
        response.set_cookie('user', '', expires=0)
        session.clear()
        return response