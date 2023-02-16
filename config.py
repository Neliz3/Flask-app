from datetime import timedelta
from dotenv import load_dotenv
import os

# Initialize environment variables
load_dotenv('/home/elizabeth/flask-app/app/.env')
admin = os.getenv("admin_email")

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.urandom(12)
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)

    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SECURE = True


class ProductConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False
