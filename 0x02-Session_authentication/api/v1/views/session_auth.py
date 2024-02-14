#!/usr/bin/env python3
"""
Module of session views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User

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
    if not User.is_valid_password(password):
         return { "error": "wrong password" }, 401
    from api.v1.auth.auth import Auth
    auth = Auth()
    return
