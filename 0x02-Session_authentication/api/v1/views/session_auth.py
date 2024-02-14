#!/usr/bin/env python3
"""
Module of session views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    email = request.form.get('email')
    password  = request.form.get('password')
    if not email or len(email) == 0:
        return { "error": "email missing" }, 400
    if not password or len(password) == 0:
        return { "error": "password missing" }, 400
    user = User.search({'email': email})
    if not user:
       return { "error": "no user found for this email" }, 404
    passw = user[0].is_valid_password(password)
    if not passw:
        return { "error": "wrong password" }, 401
    from api.v1.app import auth
    id  = user[0].to_json()['id']
    sess_id = auth.create_session(id)
    result = jsonify(user[0].to_json())
    result.set_cookie(getenv('SESSION_NAME'), sess_id)
    return result