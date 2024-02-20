#!usr/bin/env python3
"""basic flask APP"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def index() -> str:
    '''index path'''
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
