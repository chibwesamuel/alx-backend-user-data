#!/usr/bin/env python3
"""
Class that inherits from auth
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """ Decodes the Base64 authorization header
        Args:
            base64_authorization_header (str): Base64 encoded header string.
        Returns:
            str: Decoded value of the Base64 header.
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except base64.binascii.Error:
            return None  # Catch specific exception for base64 decoding error

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """ Extracts the user credentials from the Base64 decoded header
        Args:
            decoded_base64_authorization_header (str): Decoded Base64 header.
        Returns:
            Tuple[str, str]: User email and password.
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str) or
                ':' not in decoded_base64_authorization_header):
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> User:
        """ Returns the User instance based on email and password
        Args:
            user_email (str): User email.
            user_pwd (str): User password.
        Returns:
            User: User instance if found, None otherwise.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        user = users[0]
        if user.is_valid_password(user_pwd):
            return user
        else:
            return None


if __name__ == "__main__":
    """Main function of the module
    """
    a = BasicAuth()
    print(a.extract_user_credentials(None))
    print(a.extract_user_credentials(89))
    print(a.extract_user_credentials("Holberton School"))
    print(a.extract_user_credentials("Holberton:School"))
    print(a.extract_user_credentials("bob@gmail.com:toto1234"))

    user_email = "test@example.com"
    user_pwd = "password"
    user = User()
    user.email = user_email
    user.password = user_pwd
    user.save()

    print(a.user_object_from_credentials(None, None))
    print(a.user_object_from_credentials(89, 98))
    print(a.user_object_from_credentials("email@notfound.com", "pwd"))
    print(a.user_object_from_credentials(user_email, "pwd"))
    print(a.user_object_from_credentials(user_email, user_pwd))
