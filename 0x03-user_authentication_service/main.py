from auth import Auth
import bcrypt
email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

id = auth.create_session(email)
user = auth.get_user_from_session_id(2)
print(user)
# print(auth.valid_login(email, "WrongPwd"))

# print(auth.valid_login("unknown@email", password))