import os
class BaseConfig(object):
    SECRET_KEY = os.environ['PERSONAL_SECRET']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    Debug = False

class DevelopmentConfig(BaseConfig):
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    Debug = True