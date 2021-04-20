# coding = utf-8
# author = mochacha
# date = 2020.12.14

# from car import Car, ElectricCar
# import car
from car import Car
from electric_car import ElectricCar
from random import randint

my_beetle = Car('volkswagen', 'beetle', '2016')
# my_beetle = car.Car('volkswagen', 'beetle', '2016')
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', '2016')
# my_tesla = car.ElectricCar('tesla', 'roadster', '2016')
print(my_tesla.get_descriptive_name())
# print(randint(1, 10))