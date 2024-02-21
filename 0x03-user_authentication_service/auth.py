#!/usr/bin/env python3
'''authentication module'''
import bcrypt
from user import User
from db import DB
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''return hashed password'''
    pas = bytes(password, 'utf-8')
    return bcrypt.hashpw(pas, bcrypt.gensalt())


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
        '''check email for login'''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if user:
            hashed = _hash_password(password)
            print(bytes(password, 'utf-8') is hashed)
            return bcrypt.checkpw(bytes(password, 'utf-8'), hashed)
