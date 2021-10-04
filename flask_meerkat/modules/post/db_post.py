import datetime

from sqlalchemy import desc

from flask_meerkat import db
from flask_meerkat.models import Post


def get_all_posts():
    return Post.query.order_by(desc(Post.id)).all()


def insert_post(post, user_id):
    db.session.add(Post(title=post['title'],
                        text=post['text'],
                        user_id=user_id))
    db.session.commit()


def find_post_by_id(post_id):
    return Post.query.get(int(post_id))


def update_post(actual_post, new_post, user_id):
    post = Post.query.get(int(actual_post.id))
    post.user_id = user_id
    post.title = new_post['title']
    post.text = new_post['text']
    post.date_posted = datetime.datetime.utcnow()
    db.session.commit()


def delete_post(post_id):
    post = Post.query.get(int(post_id))
    db.session.delete(post)
    db.session.commit()
