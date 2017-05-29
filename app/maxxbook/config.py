import os

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'development key'
    USERNAME = 'admin'
    PASSWORD = 'default'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres@postgres:5432/maxxbook_dev'