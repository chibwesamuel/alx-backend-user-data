#!/usr/bin/env python3

from db import DB
from bcrypt import checkpw, gensalt, hashpw


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> None:
        """Register a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.
        """
        try:
            self._db.add_user(email, self._hash_password(password))
        except ValueError:
            raise ValueError(f"User {email} already exists")

    def _hash_password(self, password: str) -> bytes:
        """Hash a password.

        Args:
            password (str): The password to hash.

        Returns:
            bytes: The hashed password.
        """
        return hashpw(password.encode('utf-8'), gensalt())

    def valid_login(self, email: str, password: str) -> bool:
        """Check if login credentials are valid.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if login credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'),
                           user.hashed_password.encode('utf-8'))
        except ValueError:
            return False
