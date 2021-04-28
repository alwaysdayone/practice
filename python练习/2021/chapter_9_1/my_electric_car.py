# coding = utf-8
# author = mochacha

from electric_car import Electric_car

my_tesla = Electric_car('tesla', 'model y', 2022)
my_tesla.descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()