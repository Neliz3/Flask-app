"""
The following code creates dependencies for Flask app and Database
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs import config
from datetime import timedelta


# Flask app
app = Flask(__name__)
app.secret_key = config.secret_key
app.permanent_session_lifetime = timedelta(minutes=5)


# Database settings
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = config.db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
