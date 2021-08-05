from datetime import datetime

from itsdangerous import TimedSerializer

from flask_meerkat import app
from flask_meerkat.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String, unique=True)
    name = db.Column('name', db.String, unique=True)
    password = db.Column('password', db.String)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def get_reset_token(self):
        serializer = TimedSerializer(app.secret_key)
        return serializer.dumps(self.id)


class Post(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    text = db.Column('text', db.String)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, text,user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

