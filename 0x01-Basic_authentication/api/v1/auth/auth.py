#!/usr/bin/env python3
"""authentication"""
from api.v1.app import app_views
from flask import request
from typing import List, TypeVar


class Auth:
    '''auth class'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''authentication require'''
        if excluded_paths and path in excluded_paths:
            return False
        if excluded_paths and path:
            for paths in excluded_paths:
                if paths.endswith('/'):
                    lan = len(paths) - 1
                    paths = paths[:lan]
                    if paths == path:
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        '''secure the api on request'''
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        '''current user method'''
        return None
