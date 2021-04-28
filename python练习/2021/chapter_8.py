# coding = utf-8
# author = mochacha

# def greet_user():
#     """文档字符串：显示简单的问候语"""
#     print("Hello!")

# greet_user()
# def greet_user(username):
#     print("Hello " + username.title() + "!")

# greet_user("liu xuyang")

# def display_message():
#     print("The chapter's learning topic is Function")
# display_message()

# def favourite_book(title):
#     print("One of my favourite book is " + title + ".")
# favourite_book('Red and Dark')
# def describe_pet(pet_name, animal_type='dog'):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('dog', 'big yellow')
# describe_pet(pet_name='big yellow', animal_type='dog')
# describe_pet('big yellow')
# def make_shirt(size, style):
#     print("\nThis is your " + style + " clothes.")
#     print("The clothes's size is " + size + ".")

# make_shirt('20', 'big')
# make_shirt(size='20', style='big')

# 返回值
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# QA = get_formatted_name('liu', 'xuyang')
# print(QA)

# def get_formatted_name(first_name, middle_name, last_name):
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name

# QA = get_formatted_name('liu', 'xu', 'yang')
# print(QA)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name

# QA_1 = get_formatted_name('liu', 'xuyang')
# QA_2 = get_formatted_name('liu', 'yang', middle_name='xu')
# print(QA_1)
# print(QA_2)

# def build_person(first_name, last_name, age=''):
    # person = {'first': first_name, 'last': last_name}
    # person = first + ' ' + last
    # if age:
    #     person['age'] = age
    # return person

# QA = build_person('liu', 'xuyang', age=24)
# print(QA)
# while True:
#     print("\nPlease tell me your name: ")
#     print("(Enter \"q\" at any time to quit)")
#     first = input("First name: ")
#     if first == 'q':
#         break
#     last = input("Last name: ")
#     if last == 'q':
#         break
    
#     format_name = build_person(first, last)
#     print("\nHello, " + format_name + "!")

# 传递列表
# def greet_users(names):
#     for name in names:
#         msg = "Hello, " + name + "!"
#         print(msg)
# usernames = ['zhang', 'wang', 'li', 'zhao']
# greet_users(usernames)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print("\nThe following models have been printed: ")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['huawei', 'apple', 'samsung', 'xiaomi']
# completed_models = []

# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)

# def show_magicians(magicians):
#     for magician in magicians:
#         print("The magician's name is: " + magician)

# def make_great(magicians):
    # for magician in magicians:
    #     magician = "the Great " + magician
    # show_magicians(magicians)
#     length = len(magicians)
#     i = 0
#     while i <= length - 1:
#         current_magician = magicians.pop(0)
#         current_magician = "the Great " + current_magician
#         magicians.append(current_magician)
#         i += 1

# magicians = ['zhang', 'wang', 'li', 'zhao']
# make_great(magicians)
# show_magicians(magicians)

# def make_pizza(**toppings):
#     print(toppings)

# make_pizza(a='1', b='2', c='3')

# import chapter_7

# chapter_7.make_pizza(12, 'mushrooms', 'extra cheese')

# from chapter_7 import make_pizza
# from chapter_7 import make_pizza as mp
# import chapter_7 as p
# from chapter_7 import *

# make_pizza(12, 'mushrooms', 'extra cheese')
# mp(12, 'mushrooms', 'extra cheese')
# p.make_pizza(12, 'mushrooms')
# make_pizza(12, 'mushrooms')
"""
    编写函数时，需要牢记几个细节。应该给函数指定一个描述性的名称，且只在其中使用小写字母和下划线。
描述性名称可以帮助你和别人明白代码想要做什么。给模块命名的时候也应该遵循上述约定。
    每一个函数都应该包含简要的描述其功能的注释，该注释应该紧跟在函数定义的后面，并采用文档字符串
格式。
    所有的import语句都应该放在文件开头，唯一例外的情况就是在文件开头使用了注释来描述整个程序。
"""