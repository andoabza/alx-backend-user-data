from auth import Auth
import bcrypt
email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

id = auth.create_session(email)
auth.destroy_session(id)
# print(auth.valid_login(email, "WrongPwd"))

# print(auth.valid_login("unknown@email", password))