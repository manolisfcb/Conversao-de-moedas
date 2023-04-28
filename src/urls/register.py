from flask_restful import Resource
from resources.keycloak import *
from flask import request


class Register(Resource):
    
    @login_required
    def get(self):
        return {'message':'register'}
    
    @login_required
    def post(self):

        # Verificar se o usuário já existe
        
        username = request.form.get('username', '')
        sobrenome = request.form.get('sobrenome', '')
        email = request.form.get('email','')
        passw = request.form.get('password','')
        
        try:
            admin = get_admin()
        except:
            return {'message':'Erro: Não foi possível conectar ao servidor do Keycloak'}, 500
        
        try:
            create_user(admin, username, email, passw)
        except Exception as e:
            return {'message':'Erro: %s' %e}, 500
    
        return {'message':'Usuário criado com sucesso'}