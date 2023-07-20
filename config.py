import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


"""Configuration parameters"""

class Config:

    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    DEBUG=False
    DEVELOPMENT=False
    TEMPLATES_FOLDER = 'templates'
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ['PROD_DB_URI']
    #SQLALCHEMY_ECHO = False
    SECRET_KEY  = os.environ['PROD_APP_SECRET']


class DevConfig(Config):
    DEBUG=True
    DEVELOPMENT=True
    TEMPLATES_FOLDER = 'templates'
    # Databaset
    SQLALCHEMY_DATABASE_URI = os.environ['DEV_DB_URI']
    SQLALCHEMY_ECHO = True
    SECRET_KEY  = os.environ['DEV_APP_SECRET']


class TestConfig(Config):
    DEBUG=True
    TESTING=True
    TEMPLATES_FOLDER = 'templates'
    SECRET_KEY  = os.environ['TEST_APP_SECRET']
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_DB_URI']
    #SQLALCHEMY_ECHO = True


config = {
    'development' : DevConfig,
    'testing' : TestConfig,
    'default' : DevConfig,
    'production' : ProdConfig,
}
