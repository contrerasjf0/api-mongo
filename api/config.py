import os


class Config(object):
    DEBUG = True
    SECRET_KEY = 'dev'
    PICUMO_DB_URI = os.environ['PICUMO_DB_URI']


class DevelopmentConfig(Config):
    DEBUG = False
