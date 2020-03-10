from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:qaconsulting@35.246.121.150/flaskapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] =  str(os.getenv('SECRET_KEY'))
db = SQLAlchemy(app)

from application import routes

