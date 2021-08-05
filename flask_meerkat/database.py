import datetime

from itsdangerous import Serializer, TimedSerializer
from sqlalchemy import desc
from flask_meerkat import db, login_manager, bcrypt, app
from flask_meerkat.models import User, Post

UTF_8 = 'utf-8'


def create_database():
    db.create_all()


def insert_user(user):
    db.session.add(User(email=user['email'],
                        name=user['username'],
                        password=bcrypt.generate_password_hash(user['password']).decode(UTF_8)))
    db.session.commit()
    db.session.close()


def update_user(user_id, username, email):
    user = User.query.filter_by(id=user_id).first()
    user.name = username
    user.email = email
    db.session.commit()
    db.session.close()


def update_user_password_by_token(token, password):
    user = get_user_by_token(token)
    user.password = bcrypt.generate_password_hash(password).decode(UTF_8)
    db.session.commit()
    db.session.close()


def get_user_by_token(token):
    s = TimedSerializer(app.secret_key)
    try:
        return User.query.get(s.loads(token))
    except Exception as e:
        print(e)
        raise ValueError


def find_user_by_mail(email):
    return User.query.filter_by(email=email).first()


def find_user_by_username(username):
    return User.query.filter_by(name=username).first()


def get_all_posts():
    return Post.query.order_by(desc(Post.id)).all()


def insert_post(post, user_id):
    db.session.add(Post(title=post['title'],
                        text=post['text'],
                        user_id=user_id))
    db.session.commit()
    db.session.close()


def find_post_by_id(post_id):
    return Post.query.get(int(post_id))


def update_post(actual_post, new_post, user_id):
    post = Post.query.get(int(actual_post.id))
    post.user_id = user_id
    post.title = new_post['title']
    post.text = new_post['text']
    post.date_posted = datetime.datetime.utcnow()
    db.session.commit()
    db.session.close()


def delete_post(post_id):
    post = Post.query.get(int(post_id))
    db.session.delete(post)
    db.session.commit()
    db.session.close()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


create_database()
