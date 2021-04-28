# coding = utf-8
# author = mochacha

from car import Car

class Battery():
    def __init__(self, battery_size=50):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 85:
            range = 240
        elif self.battery_size == 50:
            range = 200
        # else:
        #     print("Your battery is to small!")
        message = "This car can go " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size =85
            
class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 10
        # 将实例用作属性
        self.battery = Battery()
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    # 重写父类方法
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")