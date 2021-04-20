# coding = utf-8
# author = mochacha
# date = 2020.12.11

# 形参是函数完成其工作所需要的一项信息，实参是调用函数时传递给函数的信息
# def greet_user(username):
#     print("Hello, " + username.title())
    
# greet_user("xuyang")
# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'name is " + pet_name.title() + ".")
    
# describe_pet("dog", "xiaobai")
# describe_pet("cat", "xiaohua")
# describe_pet(animal_type="panda", pet_name="xiaohuang")
# describe_pet(pet_name="xiaohei", animal_type="snap")
# 默认参数应该写在非默认参数的后面
# def describe_pet(animal_type, pet_name="xiaohei"):
#     print("My " + animal_type + "'s name is " + pet_name.title())
# describe_pet("dog", "XIAOHUA")
# def get_formmated_name(first_name, last_name, middle_name=""):
#     """返回整洁的姓名"""
#     # full_name = first_name + " " + last_name
#     # return full_name.title()
#     if middle_name:
#         full_name = first_name + " " + middle_name + " " + last_name
#         return full_name.title()
#     else:
#         full_name = first_name + " " + last_name
#         return full_name.title()
# name = get_formmated_name("liu", "yang", middle_name="xu")
# print(name)
def build_person(first_name, last_name, age=""):
    """返回一个字典，其中包含有关一个人的信息"""
    # person = {"first_name":first_name, "last_name":last_name}
    # if age:
        # person["age"] = age
    # person = first_name + last_name
    # return person

# message = build_person("liu", "xuyang", 33)
# print(message)
# while True:
#     print("\nPlease tell me your name: ")
#     print("Enter 'q' at any time to quit.\n" )
    
#     f_name = input("First name: ")
#     if f_name == "q":
#         break
#     l_name = input("Last name: ")
#     if l_name =="q":
#         break
#     formatted_name = build_person(f_name, l_name)
#     print("Hello, " + formatted_name + ".")

# def greet_users(names):
#     for name in names:
#         mags = "Hello " + name.title() + "!"
#         print(mags)
        
# usernames = ['zhang', 'wang', 'li', 'zhao']
# greet_users(usernames)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_model = unprinted_designs.pop()
#         print("Printing models: " + current_model)
#         completed_models.append(current_model)

# def show_completed_models(completed_models):
#     print("\nThe following models have been printed: ")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['iPhone', 'Android', 'Windows Phone', 'BlackBerry']
# completed_models = []

# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)
# 使用任意数量的位置实参
# def make_pizza(*toppings):
#     print(toppings)
    
# make_pizza('1')
# make_pizza('1', '2', '3', '4')
# 使用任意数量的关键字实参
def build_file(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_file('liu', 'xuyang', age=23, height=180)
print(user_profile)   