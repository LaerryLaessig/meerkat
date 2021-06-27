from flask import render_template, request, jsonify, session, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from flask_meerkat import app, bcrypt
from flask_meerkat.database import find_user_by_mail, insert_user


@app.route('/', methods=['GET'])
def first_page():
    return render_template('signin.html')


@app.route('/health')
def health_check():
    return {"status": "ok"}


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        user = find_user_by_mail(request.form.get('email'))
        if user and bcrypt.check_password_hash(
                user.password, request.form.get('password')):
            session['logged_in'] = True
            return render_template('userpage.html')
        else:
            return render_template('fail.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        if find_user_by_mail(request.form.get('email')) is None and \
                request.form.get('password') == request.form.get('confirm_password'):
            insert_user(request.form)
            return redirect(url_for('signin'))
        else:
            abort(401)


@app.route('/health', methods=['GET'])
def get_health():
    return {'status': 'ok'}
