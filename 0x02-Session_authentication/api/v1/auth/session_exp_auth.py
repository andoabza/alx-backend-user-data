#!/usr/bin/env python3
"""
Module of session expiration
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    '''session expiration'''
    def __init__(self):
        '''initialize expire time'''
        if isinstance(getenv('SESSION_DURATION'), int):
            self.session_duration = getenv('SESSION_DURATION')
        self.session_duration = 0

    def create_session(self, user_id=None):
        '''create session'''
        id = super().create_session(user_id)
        if id is None:
            return None
        self.user_id_by_session_id.update({id: {
            'user_id': user_id,
            'created_at': datetime.now()
        }})
        return id

    def user_id_for_session_id(self, session_id=None):
        '''using user id find session id'''
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if self.session_duration <= 0:
            return session_dict.get(session_id)
        if 'created_at' not in session_dict:
            return None
        if session_dict.get('created_at') + timedelta(
                seconds=60) > datetime.datetime.now():
            return None
        return session_dict.get('user_id')
