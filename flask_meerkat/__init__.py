import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

USER_ADMIN = os.getenv('USER_ADMIN')
PWD_ADMIN = os.getenv('PWD_ADMIN')

IMAGE_FOLDER = os.path.join('flask_quiz', 'static', 'images')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meerkat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config.update(MAIL_SERVER='smtp.gmail.com',
                  MAIL_PORT=465,
                  MAIL_USE_SSL=True,
                  MAIL_DEFAULT_SENDER=os.getenv('MAIL_DEFAULT_SENDER'),
                  MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
                  MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'))
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'signin'
login_manager.login_message_category = 'info'

mail = Mail(app)

Bootstrap(app)

db = SQLAlchemy(app)

from flask_meerkat import database
from flask_meerkat import models
from flask_meerkat import forms
from flask_meerkat import routes

database.create_database()
