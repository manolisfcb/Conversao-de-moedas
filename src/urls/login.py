from flask_restful import Resource
from resources.keycloak import *
from flask import make_response,session, jsonify, request, current_app

class Login(Resource):
    
    def get(self):


        username = request.json['username']
        passw = request.json['password']
        url = current_app.config.get('KEYCLOAK_URL')
        try:
            oidc = get_oidc()
        except:
            return {'message':'Erro: Não foi possível conectar ao servidor do Keycloak'}, 500
        
        if 'access_token' in session:
            at = session['access_token']
            token_info = oidc.introspect(at)
            if token_info['active']:
                return {'message':'Usuário já logado'}
                    
        try:
            token = get_token(oidc, username=username, password=passw)
        except Exception as e:
            return {'message':'Erro: %s' %e}, 500
        
        response = make_response(jsonify({'message': 'Login realizado com sucesso'}))
        prefered_username = get_userinfo(token['access_token'])['preferred_username']
       
        if token:
            response.set_cookie('access_token', token['access_token'])
            response.set_cookie('user', prefered_username)
            session['access_token'] = token['access_token']
            session['username'] = prefered_username
        
        return response
