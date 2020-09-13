import os
class BaseConfig(object):
    SECRET_KEY = 'KrQw9f9KcWUkAG3V'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    Debug = False

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    Debug = True