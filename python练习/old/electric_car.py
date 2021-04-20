# coding = utf-8
# author = mochacha
# date = 2020.12.14

"""
Battery():              一个模拟电动汽车电瓶的类
describe_battery():     打印一条描述电瓶容量的信息
get_range():            打印一条描述电瓶续航里程的信息
"""

from car import Car

class Battery():
    def __init__(self, battery_size=60):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -KWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)
    
"""
ElectricCar():          模拟电动汽车独特之处的类
"""
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()