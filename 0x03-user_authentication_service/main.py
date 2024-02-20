from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()
user = auth.register_user(email, password)
print([user for user in user])
user = auth.register_user(email, password)
print(len(user))

# try:
#     user = auth.register_user(email, password)
#     print("successfully created a new user!")
# except ValueError as err:
#     print("could not create a new user: {}".format(err))
# try:
#     user = auth.register_user(email, password)
#     print("successfully created a new user!")
# except ValueError as err:
#     print("could not create a new user: {}".format(err))        
# try:
#     user = auth.register_user('email', 'password')
#     print("successfully created a new user!")
# except ValueError as err:
#     print("could not create a new user: {}".format(err))        
# try:
#     user = auth.register_user('email', 'password')
#     print("successfully created a new user!")
# except ValueError as err:
#     print("could not create a new user: {}".format(err))  
