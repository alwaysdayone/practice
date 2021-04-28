# coding = utf-8
# author = mochacha

# 用户输入和while循环
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nRnter 'quit to end the program. "
# message = ""
# while message != "quit":
#     message = input(prompt)
#     # print(message)
#     if message != "quit":
#         print(message)

# 使用标志
# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)
# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(message)
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 1:
#         continue
#     print(current_number)
# x = 1
# while x <= 5:
#     print(x)
#     x += 1
# Question
# prompt = "\nWhat would you like to add in pizza? "
# prompt += "\nEnter the 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print("We will add the " + message + ".")
# import time

# prompt = "\nHow old are you? "
# while True:
#     age = input(prompt)
#     age = int(age)
#     if age < 3:
#         print("Your ticket cost free!")
#     elif age <= 12:
#         print("Your ticket cost $10!")
#     elif age > 12:
#         print("Your ticket cost $15!")
#     time.sleep(2)
# unconfirmed_users = ['zhang', 'wang', 'li']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verfying user: " + current_user.title())
#     confirmed_users.append(current_user)
# print("The following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
# pets = ['cat', 'cat', 'dog', 'cat']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# responses = {}
# active = True
# while active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response
    
#     repeat = input("Would you like to let another person respond?(yes/no) ")
#     if repeat == 'no':
#         active = False
# print("\n--- Results ---")
# for name, response in responses.items():
#     print(name.title() + " would like to climb " + response + ".")

# Question
# sandwich_orders = ['sandwich_1', 'sandwich_2', 'sandwich_3']
# finished_sandwich = []
# while sandwich_orders:
#     making_sandwich = sandwich_orders.pop()
#     print("\nMaking the sandwich " + making_sandwich)
#     finished_sandwich.append(making_sandwich)
#     print("I made your " + making_sandwich + ".")

# print("\nThe following is your ordered sandwichs:")
# for sandwich in finished_sandwich:
#     print(sandwich.title())

# print("The pastrami sandwich had sell done!")
# sandwich_orders = ['sandwich_1', 'sandwich_2', 'sandwich_3', 'pastrami', 'pastrami', 'pastrami']
# finished_sandwichs = []
# while sandwich_orders:
#     while 'pastrami' in sandwich_orders:
#         sandwich_orders.remove('pastrami')
#     making_sandwich = sandwich_orders.pop()
#     finished_sandwichs.append(making_sandwich)
#     print("\nI made your " + making_sandwich + ".")
# print("\nThe following is your ordered sandwiches:")
# for sandwich in finished_sandwichs:
#     print(sandwich.title())

# def make_pizza(size, *toppings):
#     print("\nMaking a " + str(size) +
#             "-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)