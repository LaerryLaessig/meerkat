from flask_meerkat.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String, unique=True)
    name = db.Column('name', db.String, unique=True)
    password = db.Column('password', db.String)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password


class Post(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    text = db.Column('text', db.String)
