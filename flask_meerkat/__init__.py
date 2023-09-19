import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_fontawesome import FontAwesome

USER_ADMIN = os.getenv('USER_ADMIN')
PWD_ADMIN = os.getenv('PWD_ADMIN')
SERVER_DOMAIN = os.getenv('SERVER_DOMAIN')

IMAGE_FOLDER = os.path.join('flask_quiz', 'static', 'images')

app = Flask(__name__)

with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
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
    fa = FontAwesome(app)

    Bootstrap(app)

    db = SQLAlchemy(app)

    import flask_meerkat.database
    from flask_meerkat import models
    import flask_meerkat.modules

    database.create_database()
