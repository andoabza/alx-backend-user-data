#/#!/usr/bin/env python3
"""basic flask APP"""
from flask import Flask, jsonify, request, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def index() -> str:
    '''index path'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', strict_slashes=False, methods=['POST'])
def users() -> str:
    '''register users'''
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    '''implement login method'''
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session = AUTH.create_session(email)
        result = jsonify({"email": email, "message": "logged in"})
        result.set_cookie('sessio_id', session)
        return result
    abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    '''implementation of logout users'''
    session = request.cookies.get('session_id')
    if AUTH.get_user_from_session_id(session):
        AUTH.destroy_session(session)
        return app.redirect('/')
    abort(403)


@app.route('/profile', methods=['GET'])
def profile() -> str:
    session = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)

@app.route('get_reset_password_token', methods=['POST'])
def get_reset_password_token() -> str:
    '''reset password token'''
    email = request.form.get('email')
    try:
        user = AUTH._db.find_user_by(email=email)
        if not user:
            token = AUTH.get_reset_password_token(email)
            return jsonify({"email": email, "reset_token": token})
        abort(403)
    except Exception:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token})


if __name__ == "__main__":
    from auth import Auth
    AUTH = Auth()
    app.run(host="0.0.0.0", port="5000", debug=True)
