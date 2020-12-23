from flask_meerkat.database import db


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String)
    firstname = db.Column('firstname', db.String)
    lastname = db.Column('lastname', db.String)

    def __init__(self, username, firstname, lastname):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    def __init__(self, user, text):
        self.user = user
        self.text = text

