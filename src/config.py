from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "xxx"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = os.getenv("DEBUG")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    ENV = os.getenv("ENV")
    TESTING = False

    # caminhos padrão
    
    # Keycloak
    KEYCLOAK_URL = os.getenv("KEYCLOAK_URL")
    KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM")
    KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
    KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")
    KEYCLOAK_TOKEN_URL = os.getenv("KEYCLOAK_TOKEN_URL")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
    ADMIN_PASS = os.getenv("ADMIN_PASS")
    PUBLIC_KEY = os.getenv("PUBLIC_KEY")

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mmedinac26@gmail.com'
    MAIL_PASSWORD = 'a+320Copiloto'