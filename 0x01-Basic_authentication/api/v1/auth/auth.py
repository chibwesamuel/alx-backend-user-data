#!/usr/bin/env python3

from typing import List
from flask import Flask, request

class Auth:
    """ Auth class for API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required for a path
        Args:
            path (str): The path to check for authentication requirement.
            excluded_paths (List[str]): List of paths excluded from
            authentication.
        Returns:
            bool: True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Get the Authorization header from the request
        Args:
            request: Flask request object.
        Returns:
            str: The value of the Authorization header.
        """
        return None

    def current_user(self, request=None):
        """ Get the current user from the request
        Args:
            request: Flask request object.
        Returns:
            TypeVar('User'): The current user.
        """
        return None


if __name__ == "__main__":
    app = Flask(__name__)
    with app.test_request_context('/'):
        a = Auth()
        print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
        print(a.authorization_header())
        print(a.current_user())
