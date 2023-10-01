import json
from datetime import datetime, timezone, timedelta
from flask_meerkat import app
from flask import request, jsonify
from flask_jwt_extended import create_access_token, unset_jwt_cookies, jwt_required, get_jwt, \
    get_jwt_identity

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response


@app.route('/api/login', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test@test" or password != "test":
        return {"msg": "Wrong email or password"}, 401

    access_token = create_access_token(identity=email)
    response = {"access_token": access_token}
    return response


@app.route('/api/health', methods=["GET"])
@jwt_required()
def health():
    return '{"status": "ok"}'


@app.route("/api/logout", methods=["POST"])
def api_logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response
