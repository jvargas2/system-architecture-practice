import os

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'development key'
    #SQLALCHEMY_DATABASE_URI = 'postgres://postgres@postgres:5432/maxxbook_dev'
    SQLALCHEMY_DATABASE_URI = os.environ['FLASK_DATABASE_URI']