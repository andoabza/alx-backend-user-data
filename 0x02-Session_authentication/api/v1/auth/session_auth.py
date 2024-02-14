#!/usr/bin/env python3
"""
Module of session authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    '''session authentication class'''

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''create session id'''
        if isinstance(user_id, str):
            id = str(uuid.uuid4())
            self.user_id_by_session_id.update({id: user_id})
            return id
