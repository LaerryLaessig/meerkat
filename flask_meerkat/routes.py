from flask import render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_meerkat.forms import SignInForm, SignUpForm, AccountForm, RequestResetForm, PostForm, PasswordResetForm
from flask_meerkat import app
from flask_login import login_user, current_user, logout_user, login_required
from flask_meerkat.database import insert_user, find_user_by_mail, update_user, get_all_posts, insert_post, \
    update_user_password_by_token, delete_post, find_post_by_id, update_post
from flask_meerkat.mail_client import send_password_reset_mail


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


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignInForm()
    if request.method == 'POST' and form.validate_on_submit():
        login_user(find_user_by_mail(form.email.data), remember=form.remember.data)
        flash(message='Successful logged in!', category='success')
        return redirect(url_for('home'))
    return render_template('signin.html', form=form)


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = AccountForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash(message='Update data!', category='success')
        update_user(current_user.id, username=form.username.data, email=form.email.data)
    else:
        form.username.data = current_user.name
        form.email.data = current_user.email
    return render_template('account.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash(message='Successful logged out!', category='success')
    return redirect(url_for('signin'))


@app.route('/reset_password', methods=['GET', 'POST'])
def request_reset_password():
    form = RequestResetForm()
    if request.method == 'POST' and form.validate_on_submit():
        token = find_user_by_mail(form.email.data).get_reset_token()
        send_password_reset_mail(form.email.data, url_for('reset_password', token=token, _external=True))
        flash(message='Send reset email to {email}!'.format(email=form.email.data), category='success')
        return redirect(url_for('signin'))
    return render_template('request_password_reset.html', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = PasswordResetForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            update_user_password_by_token(token, form.password.data)
            flash(message='Password changed', category='success')
            return redirect(url_for('signin'))
        except ValueError:
            flash(message='Invalid token', category='danger')
            return redirect(url_for('request_reset_password'))
    return render_template('reset_password.html', token=token, form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        insert_user(form.data)
        flash(message='Account created for {username}!'.format(username=form.username.data), category='success')
        return redirect(url_for('signin'))
    return render_template('signup.html', form=form)


@app.route('/health', methods=['GET'])
def get_health():
    return {'status': 'ok'}
