#!/usr/bin/env python3
"""
Class that inherits from auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic authentication class
    Inherits from Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracts the Base64 part of the Authorization header for Basic
        Authentication
        Args:
            authorization_header (str): The Authorization header string.
        Returns:
            str: The Base64 part of the Authorization header.
        """
        if authorization_header is None or not isinstance(
                authorization_header, str
        ) or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[-1]


if __name__ == "__main__":
    """Main function of the module
    """
    a = BasicAuth()
    print(a.extract_base64_authorization_header(None))
    print(a.extract_base64_authorization_header(89))
    print(a.extract_base64_authorization_header("Holberton School"))
    print(a.extract_base64_authorization_header("Basic Holberton"))
    print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
    print(a.extract_base64_authorization_header
          ("Basic SG9sYmVydG9uIFNjaG9vbA=="))
    print(a.extract_base64_authorization_header("Basic1234"))
