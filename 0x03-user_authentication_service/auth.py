#!/usr/bin/env python3
'''authentication module'''
import bcrypt
from user import User
from db import DB
from sqlalchemy import select


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
        rec = self._db._session.query(User).all()
        new_dict = {}
        for obj in rec:
            if '_sa_instance_state' in obj.__dict__:
                del obj.__dict__['_sa_instance_state']
            new_dict[obj.id] = obj.__dict__
        if len(new_dict) == 0:
            users = self._db.add_user(email=email, hashed_password=hashed)
            return users
        if email in new_dict:
            raise ValueError(f'User {email} already exists')
        users = self._db.add_user(email=email, hashed_password=hashed)
        return new_dict
