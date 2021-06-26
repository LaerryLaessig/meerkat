from flask import render_template, request, jsonify, session

from flask_meerkat import app, bcrypt
from flask_meerkat.database import insert_user, find_user_by_mail


@app.route('/', methods=['GET'])
def first_page():
    return render_template('login.html')


@app.route('/health')
def health_check():
    return {"status": "ok"}


@app.route('/user', methods=['POST', 'PUT'])
def add_user():
    json_data= request.json
    print(json_data)
    if find_user_by_mail(json_data['email']) is None:
        insert_user(json_data)
        status = 'success'
    else:
        status = 'this email is already registered'
    return jsonify({'result': status})


@app.route('/login', methods=['POST'])
def login():
    json_data = request.json
    user = find_user_by_mail(json_data['email'])
    if user and bcrypt.check_password_hash(
            user.password, json_data['password']):
        session['logged_in'] = True
        status = True
    else:
        status = False
    return jsonify({'result': status})


@app.route('/api/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})


@app.route('/health', methods=['GET'])
def get_health():
    return {'status': 'ok'}
