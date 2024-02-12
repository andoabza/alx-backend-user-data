#!/usr/bin/env python3
"""basic authentication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''basic auth'''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''extract base64'''
        word = 'Basic '
        if isinstance(authorization_header, str):
            if authorization_header.startswith(word):
                return authorization_header[len(word):]
        return None
