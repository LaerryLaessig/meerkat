from flask import render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_meerkat.forms import SignInForm, SignUpForm, AccountForm, PasswordResetForm
from flask_meerkat import app
from flask_login import login_user, current_user, logout_user, login_required
from flask_meerkat.database import insert_user, find_user_by_mail, update_user
from flask_meerkat.mail_client import send_password_reset_mail


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


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


@app.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    form = PasswordResetForm()
    if request.method == 'POST' and form.validate_on_submit():
        send_password_reset_mail(form.email.data)
        flash(message='Send reset email to {email}!'.format(email=form.email.data), category='success')
        return redirect(url_for('signin'))
    return render_template('password_reset.html', form=form)


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
