import json
from datetime import datetime, timezone, timedelta
from flask_meerkat import app, bcrypt
from flask import request, jsonify
from flask_jwt_extended import create_access_token, unset_jwt_cookies, jwt_required, get_jwt, \
    get_jwt_identity
from flask_meerkat.database import get_user_by_mail, get_username_by_user_id, get_whitelist, insert_whitelist_email, \
    delete_whitelist_by_id, get_user_email_by_user_id
from flask_meerkat.modules.post.db_post import get_all_posts


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(hours=1))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        return response


@app.route('/api/login', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = get_user_by_mail(email)
    if user is None or not bcrypt.check_password_hash(user.password, password):
        return {"msg": "Wrong email or password"}, 401

    access_token = create_access_token(identity=email)
    response = {"access_token": access_token}
    return response


@app.route("/api/logout", methods=["POST"])
def api_logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@app.route('/api/post', methods=['GET'])
@jwt_required()
def get_posts():
    posts = [{
        'id': p.id,
        'title': p.title,
        'text': p.text,
        'creator': get_username_by_user_id(p.user_id)} for p in get_all_posts()]
    return posts


@app.route('/api/whitelist', methods=['POST'])
@jwt_required()
def add_item_to_whitelist():
    email = request.json.get("email", None)
    insert_whitelist_email(email)
    return {"msg": f"add {email} to whitelist"}, 201


@app.route('/api/whitelist', methods=['GET'])
@jwt_required()
def get_whitelist_items():
    whitelist = [{
        'id': w.id,
        'email': w.email} for w in get_whitelist()]
    return whitelist


@app.route('/api/whitelist/<whitelist_id>', methods=['DELETE'])
@jwt_required()
def delete_whitelist_item(whitelist_id):
    if get_jwt_identity() == get_user_email_by_user_id(1):
        delete_whitelist_by_id(whitelist_id)
    return '', 204

