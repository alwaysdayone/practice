# coding = utf-8
# author = mochacha
# date = 2020.12.14

"""
Car():                  一个可用于表示汽车的类
get_descriptive_name(): 返回整洁的描述性名称
read_odometer():        打印一条信息，指出汽车行驶的里程
update_odometer():      将里程表读书设置为指定的值，拒绝回拨里程表
increment_odometer():   将里程表读数增加指定的量
"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

# """
# Battery():              一个模拟电动汽车电瓶的类
# describe_battery():     打印一条描述电瓶容量的信息
# get_range():            打印一条描述电瓶续航里程的信息
# """
# class Battery():
#     def __init__(self, battery_size=60):
#         self.battery_size = battery_size
    
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + " -KWh battery.")
    
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         message = "This car can go approximately " + str(range) + " miles on a full charge."
#         print(message)
    
# """
# ElectricCar():          模拟电动汽车独特之处的类
# """
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()