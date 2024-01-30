#!/usr/bin/env python3

from flask import Flask, request, jsonify, redirect
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


@app.route("/sessions", methods=["POST"])
def sessions() -> tuple:
    """Login a user

    Returns:
        tuple: JSON response with login status and message
    """
    email: str = request.form.get("email")
    password: str = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        return jsonify({"message": "invalid email or password"}), 401


@app.route("/sessions", methods=["DELETE"])
def delete_session() -> tuple:
    """Logout a user

    Returns:
        tuple: JSON response with logout status
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        return jsonify({"message": "invalid session ID"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
