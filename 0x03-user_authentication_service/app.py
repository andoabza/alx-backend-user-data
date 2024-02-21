#!/usr/bin/env python3
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


if __name__ == "__main__":
    from auth import Auth
    AUTH = Auth()
    app.run(host="0.0.0.0", port="5000")
