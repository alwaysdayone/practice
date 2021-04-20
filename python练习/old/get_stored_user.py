# coding = utf-8
# author = mochacha
# date = 2020.12.15

import json

def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except:
        return None
    else:
        return username