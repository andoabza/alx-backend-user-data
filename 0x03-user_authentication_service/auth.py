#!/usr/bin/env python3
'''authentication module'''
import bcrypt
from user import User
from db import DB
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''return hashed password'''
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
   

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
            return bcrypt.checkpw(password.encode('utf-8'), bytes(pas, 'utf-8'))
        return False
