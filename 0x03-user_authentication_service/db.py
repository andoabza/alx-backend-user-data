#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import TypeVar
from sqlalchemy.exc import NoResultFound, InvalidRequestError

from user import Base
from user import User as user


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine(
            "mysql+mysqldb://root:root@localhost/school_db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> user:
        """add user into the database"""
        try:
            new_user = user(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwarg: dict) -> user:
        '''find user by arg'''
        for key in kwarg:
            key = key
            value = kwarg[key]
        base = user.__dict__
        if key in base:
            user_data = base[key]
            users = self._session.query(user).filter(user_data == value).one()
            if users:
                return users
        raise InvalidRequestError
        

    def update_user(self, user_id: int, **kwarg: dict) -> None:
        '''update user based on id'''
        updated = self.find_user_by(id=user_id)
        if 'email' in kwarg:
            value = kwarg.get('email')
            updated.email = value
        if 'hashed_password' in kwarg:
            value = kwarg.get('hashed_password')
            updated.hashed_password = value
        if 'session_id' in kwarg:
            value = kwarg.get('session_id')
            updated.session_id = value
        if 'reset_token' in kwarg:
            value = kwarg.get('reset_token')
            updated.reset_token = value
        self._session.commit()
