from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

email = 'test@test.com'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)
v = my_db.find_user_by(id=user.id)
try:
    print('old', v.hashed_password)
    my_db.update_user(user.id, hashed_password='NewPwd')
    print("Password updated", v.hashed_password)
except ValueError:
    print("Error")