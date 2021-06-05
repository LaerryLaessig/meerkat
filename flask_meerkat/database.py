from flask_meerkat import db, bcrypt
from flask_meerkat.models import User, List, ListUserRelationship, ListItemRelationship


def create_database():
    db.create_all()


def insert_user(user):
    db.session.add(User(email=user['email'],
                        name=user['name'],
                        password=bcrypt.generate_password_hash(user['password']).decode('utf-8')))
    db.session.commit()
    db.session.close()


def find_user_by_mail(email):
    return User.query.filter_by(email=email).first()


def insert_list(list_name):
    db.session.add(List(name=list_name))
    db.session.commit()
    db.session.close()


def insert_list_relationship(list_id, user_id):
    db.session.add(ListUserRelationship(list_id=list_id, user_id=user_id))
    db.session.commit()
    db.session.close()


def insert_list_item_relationship(list_id, item_id):
    db.session.add(ListItemRelationship(list_id=list_id, item_id=item_id))
    db.session.commit()
    db.session.close()


create_database()
