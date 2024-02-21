from auth import Auth
import bcrypt
email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, "WrongPwd"))

print(auth.valid_login("unknown@email", password))
# pas = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
# print(bcrypt.checkpw(bytes(password, 'utf-8'), pas))
# print(bcrypt.checkpw(bytes('password', 'utf-8'), pas))
