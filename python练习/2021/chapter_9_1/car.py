# coding = utf-8
# author = mochacha

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10
    
    def descriptive_name(self):
        print(str(self.year) + ' ' + self.make + ' ' + self.model)
        
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back the odometer!")
    
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("The miles can't less 0")
            
    def fill_gas_tank(self):
        print("Please fill the gas tank full!")