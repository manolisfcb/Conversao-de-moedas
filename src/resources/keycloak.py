from keycloak import KeycloakAdmin, KeycloakOpenID
from flask import current_app, session, redirect, url_for
from functools import wraps
from .exceptions import InvalidTokenError
import jwt
from flask import request

def get_token_request():

    headers = request.headers
    if 'Authorization' not in headers.keys():
        raise InvalidTokenError('Token não encontrado')
    try:
        access_token = headers['Authorization'].split(' ')[1]
    except Exception as e:
        raise InvalidTokenError(f'{e}')
    return access_token 


def get_admin():
    """
    It creates a KeycloakAdmin object.
    :return: A KeycloakAdmin object
    """
    return KeycloakAdmin(server_url=current_app.config.get('KEYCLOAK_URL'),
                         username=current_app.config.get('ADMIN_USERNAME'),
                         password=current_app.config.get('ADMIN_PASS'),
                         realm_name=current_app.config.get('KEYCLOAK_REALM'),
                         verify=True)



def create_user(admin, username, email, password):
    """
    It creates a user.

    :param admin: The admin object that you created in the previous step
    :param username: The username of the user you want to create
    :param email: The email address of the user
    :param password: The password for the user
    :return: A user object.
    """
    return admin.create_user({"email": email,
                              "username": username,
                              "credentials": [{"value": password, "type": "password", }],
                              "enabled": True,
                              "realmRoles": ["user", ]})


def get_oidc():
    """
    It creates a KeycloakOpenID object.
    :return: A KeycloakOpenID object
    """
    return KeycloakOpenID(server_url=current_app.config.get('KEYCLOAK_URL'),
                          client_id=current_app.config.get('KEYCLOAK_CLIENT_ID'),
                          realm_name=current_app.config.get('KEYCLOAK_REALM'),
                          client_secret_key=current_app.config.get('KEYCLOAK_CLIENT_SECRET'),
                          verify=True)


def get_token(oidc_obj, username, password):
    """
    It takes a username and password, and returns a token
    
    :param oidc_obj: The object returned by the get_oidc() function
    :param username: The username of the user you want to authenticate
    :param password: The password of the user
    :return: A token
    """

    return oidc_obj.token(username, password)


def check_token(access_token):
    """
    It takes an access token, checks it against the OIDC provider, and returns True if the token is
    valid
    
    :param access_token: The access token you want to check
    :return: True if the token is valid, False otherwise:
    """
    oidc = get_oidc()
    token_info = oidc.introspect(access_token)
    if token_info.get('active'):
        return True
    return False


def get_userinfo(access_token):
    """
    It takes an access token and returns the user info
    
    :param access_token: The access token you got from the previous step
    :return: A dictionary of user information.
    """
    oidc = get_oidc()
    try:
        return oidc.userinfo(access_token)
    except Exception as e:
        print("Exception occurs: %s" % e)
    return None


def login_required(f):
    """
    If the access_token is in the session, and the token is valid, then return the function that was
    passed in. Otherwise, redirect to the login page
    
    :param f: The function to be decorated
    :return: A function that takes in a function as an argument.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = get_token_request()
        try:
            if is_valid(token):
                return f(*args, **kwargs)
            return {'message': f'{e}'}, e.status_code
        except Exception as e:
            return {'message': f'{e}'}, e.status_code
    return decorated_function

def delete_user(admin, username):
    """
    It deletes a user
    
    :param admin: The admin object that you created in the previous step
    """
    admin.delete_user(username)
    return None

def is_valid(token):
    flag = decode_token(token)
    
    if flag:
        return True
    else:
        return False

def decode_token(access_token):
    public_key = current_app.config['PUBLIC_KEY']
    public_key = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
    
    try:
        token_decodificadao = jwt.decode(access_token,public_key,audience=['Currency', 'Currency-converter', 'account'], algorithms=['RS256'])
        return token_decodificadao
    except Exception as e:
        raise InvalidTokenError(f'{e}')
    
