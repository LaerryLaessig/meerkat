from flask import render_template, request, url_for
from flask_login import current_user
from werkzeug.utils import redirect
from flask_meerkat import app
from .db_post import insert_post, get_all_posts, \
    delete_post, find_post_by_id, update_post
from flask_meerkat.modules.post.forms_post import PostForm


@app.route('/', methods=['GET', 'POST'])
def home():
    posts = get_all_posts()
    return render_template('home.html', posts=posts)


@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if request.method == 'POST':
        insert_post(form.data, current_user.id)
        return redirect(url_for('home'))
    return render_template('post.html', form=form)


@app.route('/post/<post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    form = PostForm()
    post = find_post_by_id(post_id)
    if request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text
        return render_template('post.html', form=form, post=post)
    elif request.method == 'POST':
        update_post(actual_post=post,
                    new_post=form.data,
                    user_id=current_user.id)
        return redirect(url_for('home'))


@app.route('/post/<post_id>/delete', methods=['POST'])
def remove_post(post_id):
    delete_post(post_id)
    return redirect(url_for('home'))
