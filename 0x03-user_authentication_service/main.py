from auth import Auth
import bcrypt
email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()
if not auth._db.find_user_by(email=email):
    auth.register_user(email, password)

# print(auth.valid_login(email, "WrongPwd"))

# print(auth.valid_login("unknown@email", password))