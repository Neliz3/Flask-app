from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import ProductConfig, DevelopmentConfig, TestingConfig

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object(ProductConfig())
elif app.config["ENV"] == "development":
    app.config.from_object(DevelopmentConfig())
else:
    app.config.from_object(TestingConfig())

db = SQLAlchemy()
db.init_app(app)


from app import admin
from app import auth
from app import general
from app import user
from app import models
