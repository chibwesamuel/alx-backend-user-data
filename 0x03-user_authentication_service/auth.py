#!/usr/bin/env python3

from typing import Union
from bcrypt import checkpw
from db import DB
from user import User


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> Union[User, None]:
        """
        Register a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            Union[User, None]: The newly created User object,
            or None if user already exists.
        """
        try:
            return self._db.add_user(email, password)
        except ValueError:
            return None

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'),
                           user.hashed_password.encode('utf-8'))
        except ValueError:
            return False
