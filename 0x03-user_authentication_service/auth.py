#!/usr/bin/env python3
"""
Auth module
"""
from db import DB
from user import User
from typing import Union

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            User: The newly registered user.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {email} already exists")
        hashed_password = _hash_password(password)
        return self._db.add_user(email, hashed_password)
