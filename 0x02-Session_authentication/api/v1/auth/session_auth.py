#!/usr/bin/env python3
"""
Module of session authentication
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    '''session authentication class'''

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''create session id'''
        if isinstance(user_id, str):
            id = str(uuid.uuid4())
            self.user_id_by_session_id[id] = user_id
            return id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''return user id  on session id'''
        if isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        '''current user'''
        cookie_id = self.session_cookie(request)
        id = self.user_id_for_session_id(cookie_id)
        return User.get(id)

    def destroy_session(self, request=None):
        '''logout'''
        if request:
            sess_id = self.session_cookie(request)
            if sess_id:
                id = self.user_id_for_session_id(sess_id)
                if id:
                    del(self.user_id_by_session_id['id'])
                    return True

        return False
