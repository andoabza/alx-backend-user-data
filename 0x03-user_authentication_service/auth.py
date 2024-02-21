#!/usr/bin/env python3
'''authentication module'''
import bcrypt
import uuid
from user import User
from db import DB
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''return hashed password'''
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    '''generate id for the user'''
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''registser users'''
        hashed = _hash_password(password)
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            users = self._db.add_user(email=email, hashed_password=hashed)
            return users
        if user.email == email:
            raise ValueError(f'User {email} already exists')
        users = self._db.add_user(email=email, hashed_password=hashed)
        return users

    def valid_login(self, email: str, password: str) -> bool:
        '''check user email and password are correct'''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if user:
            pas = user.hashed_password
            return bcrypt.checkpw(
                password.encode('utf-8'), bytes(pas, 'utf-8'))
        return False

    def create_session(self, email: str) -> str:
        '''create session id for users based on email'''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                gen_id = _generate_uuid()
                self._db.update_user(user.id, session_id=gen_id)
                return user.session_id
        except NoResultFound:
            return
