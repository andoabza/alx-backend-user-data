#!/usr/bin/env python3
"""basic authentication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''basic auth'''
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''extract base64'''
        if authorization_header is None:
            return None
        if authorization_header is not str:
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header[5:]
        return None
    