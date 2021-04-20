# coding = utf-8
# author = mochacha
# date = 2020.12.15

import json

def get_new_username():
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
    return username
