from flask import render_template, request, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import redirect

from flask_meerkat import app
from flask_meerkat.database import insert_user, get_user_by_mail, update_user, update_user_password_by_token, \
    insert_whitelist_email, \
    count_user, get_whitelist_by_email
from .forms_user import SignInForm, SignUpForm, AccountForm, RequestResetForm, PasswordResetForm
from .mail.mail_client import send_password_reset_mail


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = AccountForm()
    if form.validate_on_submit():
        flash(message='Update data!', category='success')
        update_user(current_user.id, username=form.username.data, new_email=form.email.data)
    else:
        form.username.data = current_user.name
        form.email.data = current_user.email
    return render_template('user/account.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignInForm()
    if form.validate_on_submit():
        login_user(get_user_by_mail(form.email.data), remember=form.remember.data)
        flash(message='Successful logged in!', category='success')
        return redirect(url_for('home'))
    return render_template('user/signin.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash(message='Successful logged out!', category='success')
    return redirect(url_for('signin'))


@app.route('/reset_password', methods=['GET', 'POST'])
def request_reset_password():
    form = RequestResetForm()
    if form.validate_on_submit():
        token = get_user_by_mail(form.email.data).get_reset_token()
        send_password_reset_mail(form.email.data, url_for('reset_password', token=token, _external=True))
        flash(message=f'Send reset email to {form.email.data}!', category='success')
        return redirect(url_for('signin'))
    return render_template('user/request_password_reset.html', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        try:
            update_user_password_by_token(token, form.password.data)
            flash(message='Password changed', category='success')
            return redirect(url_for('signin'))
        except ValueError:
            flash(message='Invalid token', category='danger')
            return redirect(url_for('request_reset_password'))
    return render_template('user/reset_password.html', token=token, form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('user/signup.html', form=form)
    if form.validate_on_submit() and \
            (count_user() == 0 or get_whitelist_by_email(form.data['email'])):
        if count_user() == 0:
            insert_whitelist_email(form.data['email'])
        insert_user(form.data)
        flash(message=f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('signin'))
    else:
        flash(message=f'Registration not allowed for {form.email.data}! Please contact admin.',
              category='danger')
    return render_template('user/signup.html', form=form)
