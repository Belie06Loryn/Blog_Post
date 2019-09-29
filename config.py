import os

class Config:
    SECRET_KEY = 'ALEXIE'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/bloger'
    UPLOADED_PHOTOS_DESK ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/bloger'
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/bloger'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/bloger_test'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}