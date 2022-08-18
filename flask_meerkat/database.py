from itsdangerous import TimedSerializer
from sqlalchemy import desc
from flask_meerkat import db, login_manager, bcrypt, app
from flask_meerkat.models import User, WhiteListEmail

UTF_8 = 'utf-8'


def create_database():
    db.create_all()


def get_all_user():
    return User.query.all()


def insert_user(user):
    db.session.add(User(email=user['email'],
                        name=user['username'],
                        password=bcrypt.generate_password_hash(user['password']).decode(UTF_8)))
    db.session.commit()


def update_user(user_id, username, new_email):
    user = User.query.filter_by(id=user_id).first()
    email = get_whitelist_by_email(user.email)
    email.email = new_email
    user.name = username
    user.email = new_email
    db.session.commit()


def update_user_password_by_token(token, password):
    user = get_user_by_token(token)
    user.password = bcrypt.generate_password_hash(password).decode(UTF_8)
    db.session.commit()


def get_user_by_token(token):
    s = TimedSerializer(app.secret_key)
    try:
        return User.query.get(s.loads(token))
    except Exception as e:
        print(e)
        raise ValueError


def get_username_by_user_id(user_id):
    return User.query.get(int(user_id)).name


def get_user_by_user_id(user_id):
    return User.query.get(int(user_id))


def get_user_by_mail(email):
    return User.query.filter_by(email=email).first()


def get_user_by_username(username):
    return User.query.filter_by(name=username).first()


def count_user():
    return User.query.count()


def get_whitelist():
    return WhiteListEmail.query.order_by(desc(WhiteListEmail.id)).all()


def insert_whitelist_email(email):
    db.session.add(WhiteListEmail(email=email))
    db.session.commit()


def get_whitelist_by_email(email):
    return WhiteListEmail.query.filter_by(email=email).first()


def delete_whitelist_by_id(whitelist_id):
    email = WhiteListEmail.query.get(int(whitelist_id))
    db.session.delete(email)
    db.session.commit()


def update_whitelist(old_email, new_email):
    email = get_whitelist_by_email(old_email)
    email.email = new_email
    db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


create_database()
