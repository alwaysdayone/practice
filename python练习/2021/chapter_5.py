# coding = utf-8
# author = mochacha
# 2021年4月20日

# import random

# for i in range(10):
#     number = random.randint(1, 10)
#     print(number)
# cars = ['bMw', 'byd', 'benchi']
# for car in cars:
#     if car.lower() == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# age_0 = 10
# age_1 = 20
# if age_0 > 5 and age_1 > 10:
#     print(True)
# else:
#     print(False)
# requesting_topping = [1,2,3,4]
# if 3 in requesting_topping:
#     print(True)
# else:
#     print(False)

# if 1 not in requesting_topping:
#     print(True)
# else:
#     print(False)
# car = 'subaru'
# print("Is car == 'subaru'? I predict True")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict False")
# print(car == 'audi')
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# else:
#     price = 10
# print("Your admission cost is $" + str(price) + '.')
# Question
# alien_colors = ['green', 'yellow', 'red']
# for alien_color in alien_colors:
#     if alien_color == 'green':
#         print("You have got " + str(5) + " points.")

# for alien_color in alien_colors:
#     if alien_color == 'gree':
#         print("You have got " + str(5) + "points.")
# available_toppings = ('mushrooms', 'olives', 'green peppers')
# requested_toppings = ['mushrooms', 'french fries']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry, we don't have " + requested_topping + ".")
# print("\nFinish making your pizza!")
# Question
# users = []
# users = ['admin', 'zhang', 'wang', 'li', 'zhao']
# if users:
#     for user in users:
#         if user.lower() == 'admin':
#             print("Hello " + user + ", would you like to see a status report?")
#         elif user.lower() != 'admin':
#             print("Hello " + user + ", thank you for logging in again!")
# else:
#     print("We need to find some users!")
# del users[0]
# print(users)
# del users[0]
# print(users)
# users.remove("wang")
# print(users)
# users.pop()
# users.pop()
# print(users)
# current_users = ['zhang', 'wang', 'li', 'Zhao', 'admin']
# new_users = ['zhao', 'qian', 'sun', 'li', 'admin']
# for name in new_users:
#     if name in current_users:
#         print("The name is already be used, please try again!")
#     elif name not in current_users:
#         print("The name can be used!")
# current_users_new = []
# for name in current_users:
#     current_users_new.append(name.lower())
# for name in new_users:
#     if name.lower() in current_users_new:
#         print("The name is already be used, please try again!")
#     else:
#         print("The name can be used!")
# numbers = []
# for i in range(1, 10):
#     numbers.append(i)
# # print(numbers)
# for number in numbers:
#     if number == 1:
#         print("1st")
#     elif number == 2:
#         print("2nd")
#     elif number == 3:
#         print("3rd")
#     else:
#         print(str(number) + "th")