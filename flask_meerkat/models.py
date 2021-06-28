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


class List(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)

    def __init__(self, name):
        self.name = name


class ListUserRelationship(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    list_id = db.Column('list_id', db.Integer)
    user_id = db.Column('user_id', db.Integer)

    def __init__(self, list_id, user_id):
        self.list_id = list_id
        self.user_id = user_id


class ListItemRelationship(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    list_id = db.Column('list_id', db.Integer)
    item_id = db.Column('item_id', db.Integer)

    def __init__(self, list_id, item_id):
        self.list_id = list_id
        self.item_id = item_id


class Item(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)

    def __init__(self, name):
        self.name = name
