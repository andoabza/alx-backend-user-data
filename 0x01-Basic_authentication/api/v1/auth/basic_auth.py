#!/usr/bin/env python3
"""basic authentication"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from encodings import utf_8
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    '''basic auth'''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''extract base64'''
        word = 'Basic '
        if isinstance(authorization_header, str):
            if authorization_header.startswith(word):
                return authorization_header[len(word):]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''base64 authorization'''
        if isinstance(base64_authorization_header, str):
            try:
                new = bytes(base64_authorization_header, 'utf-8')
                result = b64decode(base64_authorization_header)
                return result.decode('utf-8')
            except Exception:
                return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """extract user credentials"""
        if isinstance(decoded_base64_authorization_header, str):
            if ':' in decoded_base64_authorization_header:
                length = len(decoded_base64_authorization_header)
                index = decoded_base64_authorization_header.find(':')
                first = decoded_base64_authorization_header[:index]
                second = decoded_base64_authorization_header[index + 1:length]
                return (first, second)
        return (None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """extract users from object"""
        if isinstance(user_email, str) and isinstance(user_pwd, str):
            user = User()
            if user.search({'email': user_email}):
                if user.is_valid_password(user_pwd):
                    return user
        return None
