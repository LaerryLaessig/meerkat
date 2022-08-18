from flask import render_template, request, url_for
from flask_login import current_user
from werkzeug.utils import redirect
from flask_meerkat import app
from .db_post import insert_post, get_all_posts, \
    delete_post, get_post_by_id, update_post
from flask_meerkat.modules.post.forms_post import PostForm
from ...database import get_username_by_user_id


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', posts=[{
        'id': p.id,
        'title': p.title,
        'text': p.text,
        'creator': get_username_by_user_id(p.user_id)} for p in get_all_posts()])


@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        insert_post(form.data, current_user.id)
        return redirect(url_for('home'))
    return render_template('post/upsert_post.html', form=form)


@app.route('/post/<post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    form = PostForm()
    post = get_post_by_id(post_id)
    if request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text
        return render_template('post/upsert_post.html', form=form, post=post)
    if form.validate_on_submit():
        update_post(actual_post=post,
                    new_post=form.data,
                    user_id=current_user.id)
        return redirect(url_for('home'))


@app.route('/post/<post_id>/delete', methods=['POST'])
def remove_post(post_id):
    delete_post(post_id)
    return redirect(url_for('home'))
