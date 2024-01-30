#!/usr/bin/env python3

from flask import Flask, request, jsonify
from auth import Auth

app: Flask = Flask(__name__)
AUTH: Auth = Auth()


@app.route("/users", methods=["POST"])
def users() -> tuple:
    """Register a user

    Returns:
        tuple: JSON response with registration status and message
    """
    email: str = request.form.get("email")
    password: str = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
