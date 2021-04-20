# coding = utf-8
# author = mochacha
# date = 2020.12.14

from car import Car

my_new_car = Car('audi', 'a6', '2020')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 20
my_new_car.read_odometer()