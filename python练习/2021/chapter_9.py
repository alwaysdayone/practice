# coding = utf-8
# author = mochacha

# 类
# class Dog():
#     """一次模拟小狗的简单尝试"""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         print(self.name.title() + " is now sitting.")
    
#     def roll_over(self):
#         print(self.name.title() + " rolled over!")
        
# my_dog = Dog('big yellow', 5)
# print("My dog's name is " + my_dog.name.title())
# print("My dog is " + str(my_dog.age) + " years old")
# my_dog.sit()
# my_dog.roll_over()

# class Restaurant():
#     def __init__(self, resturant_name, cuisine_type):
#         self.resturant_name = resturant_name
#         self.cuisine_type = cuisine_type
    
#     def describe_resturant(self):
#         print("The resturant name is: " + self.resturant_name)
#         print("The resturant cuisine type is: " + self.cuisine_type)
    
#     def open_resturant(self):
#         print("\nThe resturant is opening now")
        
# restaurant = Restaurant('shanximianguan', 'shanxi')
# print(restaurant.resturant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_resturant()
# restaurant.open_resturant()

# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 10
    
#     def descriptive_name(self):
#         print(str(self.year) + ' ' + self.make + ' ' + self.model)
        
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
        
#     def update_odometer(self, miles):
#         if miles >= self.odometer_reading:
#             self.odometer_reading = miles
#         else:
#             print("You can't roll back the odometer!")
    
#     def increment_odometer(self, miles):
#         if miles >= 0:
#             self.odometer_reading += miles
#         else:
#             print("The miles can't less 0")
            
    # def fill_gas_tank(self):
    #     print("Please fill the gas tank full!")

# new_car = Car('bmw', '325Li', 2021)
# new_car.descriptive_name()
# print(new_car.odometer_reading)
# new_car.read_odometer()
# new_car.update_odometer(15)
# new_car.read_odometer()
# new_car.increment_odometer(8)
# new_car.read_odometer()

# class Battery():
#     def __init__(self, battery_size=50):
#         self.battery_size = battery_size
    
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
#     def get_range(self):
#         if self.battery_size == 85:
#             range = 240
#         elif self.battery_size == 50:
#             range = 200
#         message = "This car can go " + str(range)
#         message += " miles on a full charge."
#         print(message)
    
#     def upgrade_battery(self):
#         if self.battery_size != 85:
#             self.battery_size =85

# 继承
# class Electric_car(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 10
#         # 将实例用作属性
#         self.battery = Battery()
    
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
#     # 重写父类方法
#     def fill_gas_tank(self):
#         print("This car doesn't need a gas tank!")

# tesla_car = Electric_car('tesla', 'model 3', 2021)
# tesla_car.descriptive_name()
# tesla_car.describe_battery()
# tesla_car.fill_gas_tank()
# tesla_car.battery.describe_battery()
# tesla_car.battery.get_range()
# tesla_car.battery.upgrade_battery()
# tesla_car.battery.get_range()

# python标准库
from collections import OrderedDict

favourite_languages = OrderedDict()
favourite_languages['zhang'] = 'java'
favourite_languages['wang'] = 'c'
favourite_languages['li'] = 'python'
favourite_languages['zhao'] = 'c#'

for name,language in favourite_languages.items():
    print(name.title() + "'s favourute language is " + language.title())