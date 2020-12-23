from sqlalchemy import asc
from flask_meerkat import db


def create_database():
    db.create_all()



create_database()
