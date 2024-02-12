#!/usr/bin/env python3
"""basic authentication"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from encodings import utf_8


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
