#!/usr/bin/env python3
"""
Implements a _generate_uuid function in the auth module.
"""

import bcrypt
import uuid
from typing import Union
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hashes a password string.

        Args:
            password (str): The password string to hash.

        Returns:
            bytes: The hashed password.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> Union[User, None]:
        """Register a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            Union[User, None]: The newly created User object,
            or None if user already exists.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(email=email,
                                     hashed_password=hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password.encode('utf-8'))
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for the user.

        Args:
            email (str): The email of the user.

        Returns:
            str: The session ID.
        """
        user = self._db.find_user_by(email=email)
        if user:
            session_id = str(uuid.uuid4())
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Retrieve user from session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            Union[User, None]: The corresponding User object or None.
        """
        if session_id:
            try:
                return self._db.find_user_by(session_id=session_id)
            except NoResultFound:
                return None
        return None

    def _generate_uuid(self) -> str:
        """Generate a UUID string.

        Returns:
            str: The generated UUID.
        """
        return str(uuid.uuid4())
