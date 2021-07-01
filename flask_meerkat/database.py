from sqlalchemy import desc

from flask_meerkat import db, login_manager, bcrypt
from flask_meerkat.models import User, Post


def create_database():
    db.create_all()


def insert_user(user):
    db.session.add(User(email=user['email'],
                        name=user['username'],
                        password=bcrypt.generate_password_hash(user['password']).decode('utf-8')))
    db.session.commit()
    db.session.close()


def update_user(user_id, username, email):
    user = User.query.filter_by(id=user_id).first()
    user.name = username
    user.email = email
    db.session.commit()


def find_user_by_mail(email):
    return User.query.filter_by(email=email).first()


def find_user_by_username(username):
    return User.query.filter_by(name=username).first()


def get_all_posts():
    return Post.query.order_by(desc(Post.id)).all()


def insert_post(post):
    db.session.expunge_all()
    db.session.add(Post(title=post['title'],
                        text=post['text']))
    db.session.commit()
    db.session.close()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


create_database()
