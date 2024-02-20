#!/usr/bin/env python3
'''authentication module'''
import bcrypt
from user import User
from db import DB
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''return hashed password'''
    hashed = password.encode('utf-8')
    hash = bcrypt.hashpw(hashed, bcrypt.gensalt())
    return hash


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
