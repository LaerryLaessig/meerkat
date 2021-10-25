from datetime import datetime

from itsdangerous import TimedSerializer
from sqlalchemy.orm import relationship

from flask_meerkat import app
from flask_meerkat.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String, unique=True)
    name = db.Column('name', db.String, unique=True)
    password = db.Column('password', db.String)
    posts = db.relationship('Post', backref='author')

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def get_reset_token(self):
        serializer = TimedSerializer(app.secret_key)
        return serializer.dumps(self.id)


class WhiteListEmail(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String)

    def __init__(self, email):
        self.email = email


class Post(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    text = db.Column('text', db.String)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id


class Task(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    subtasks = relationship('Subtask', back_populates='task')
    reviser_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, reviser_id, subtasks, creator_id):
        self.title = title
        self.subtasks = subtasks
        self.reviser_id = reviser_id
        self.creator_id = creator_id


class Subtask(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    status = db.Column('status', db.String)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id', ondelete='CASCADE'))
    task = relationship('Task', back_populates='subtasks')

    def __init__(self, name, status):
        self.name = name
        self.status = status


