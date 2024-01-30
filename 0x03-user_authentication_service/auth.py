#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt

    Args:
        password (str): The password to hash

    Returns:
        bytes: The hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())