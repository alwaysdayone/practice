# coding = utf-8
# author = mochacha
# date = 2020.12.15

import get_stored_user, get_new_user

def greet_user():
    username = get_stored_user.get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_user.get_new_username()
        print("I'll remember you when you come next time.")
        
greet_user()