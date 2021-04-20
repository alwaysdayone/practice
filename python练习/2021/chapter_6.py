# coding = utf-8
# author = mochacha
# 2021年4月20日

# 字典
# alien_0 = {'color':'green', 'points':5, 'test':(1, 2, 3)}
# print(alien_0['color'])
# print(alien_0['points'])
# print(alien_0['test'])
# alien_0 = {}
# alien_0['color'] = 'green'
# # print(alien_0)
# alien_0['points'] = 5
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# # print(alien_0)
# print("The alien is " + alien_0['color'] + ".")
# alien_0['color'] = 'yellow'
# # print(alien_0)
# print("The alien is " + alien_0['color'] + ".")
# del alien_0['points']
# print(alien_0)
# print("The alien's color is " + 
#         alien_0['color'] + ".")
# personal_messgae = {}
# personal_messgae['first_name'] = 'liu'
# personal_messgae['last_name'] = 'xuyang'
# personal_messgae['age'] = 24
# personal_messgae['gender'] = 'male'
# personal_messgae['city'] = 'beijing'
# print(personal_messgae)
# for key, value in personal_messgae.items():
#     print(key + ": " + str(value))

# number_dict = {'zhang': 3, 'wang': 1, 'li': 6, 'zhao': 2, 'liu': 5, 'admin': 8}
# print("What is your favourite number? I predict 3.")
# print("zhang favourite number is " + str(number_dict['zhang']))

# for key in number_dict.keys():
#     print(key)
# for value in number_dict.values():
#     print(value)
# for key, value in number_dict.items():
#     print(key + ": " + str(value))

# user_0 = {
#     'username': 'admin',
#     'first': 'liu',
#     'last': 'xuyang',
#     'last2': 'xuyang'
#     }
# 打印键时keys()可以省略, 打印值时values()不可省略.
# for message in user_0.keys():
#     print(message)
# for message in user_0:
#     print(message)
# for message in sorted(user_0.keys()):
#     print(message.title() + ", thank you!")
# for message in set(user_0.values()):
#     print(message)
# numbers = (1,1,2,2,3,4,5)
# for number in set(numbers):
#     print(number)

# rivers = {
#     'nile': 'egypt',
#     'mississippi river': 'mexico',
#     'changjiang': 'china'
#     }
# for river, country in rivers.items():
#     print("The " + river + " runs throuth " + country + ".\n")
# for river in rivers.keys():
#     print("The river's name is " + river.title() + ".\n")
# for country in rivers.values():
#     print("The country's name is " + country.title() + ".\n")

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print("Total number of aliens: " + str(len(aliens)))

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
        
# for alien in aliens[:5]:   
#     print(alien)
# print("...")
# print("Total number of aliens: " + str(len(aliens)))

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
#     }
# print(pizza['toppings'])
# print("Your ordered a " + pizza['crust'] + "-crust pizza " + 
#         "with the following toppings: ")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# users = {
#     "liu xuyang": {
#         'first': 'liu',
#         'last': 'xuyang',
#         'location': 'beijing'
#         },
#     "zhang jianxi": {
#         'first': 'zhang',
#         'last': 'jianxi',
#         'location': 'xingtai'
#         }
#     }

# for user_name, user_info in users.items():
#     print("\nUsername: " + user_name)
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
    
#     print("\tFull name: " + full_name.title())
#     print("\tLocation: " + location.title())