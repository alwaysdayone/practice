# coding = utf-8
# author = mochacha
# date = 2020.12.15

def get_formatted_name(first, last, middle=''):
    # full_name = first + ' ' + last
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()