# coding = utf-8
# author = mochacha
# date = 2020.12.07

# cars = ["bmw", "xiaopeng", "tesla"]
# for car in cars:
    # if car.title() == "Bmw":
    #     print(car.upper())
    # else:
    #     print(car.title())
    # if car != "bmw":
    #     print(car.title())
    # else:
    #     print(car.upper())
# 比较数字 == != > < >= <=
# age = 23
# if age > 22 and age < 24:
#     print("yes")
# else:
#     print("no")
# if (age>22) and (age<24):
#     print("yes")
# if (age>24) or (age<30):
#     print("yes")
# cars = ["bmw", "xiaopeng", "tesla"]
# if "bmw" not in cars:
#     print("not in")
# elif "bmw" in cars:
#     print("in")
# else:
#     print("error")
# toppings = []
# if len(toppings)==0:
#     print("empty")
# else:
#     print("not empty")
# dict练习
# alien = {"color":"green", "points":5}
# print(alien)
# print(alien["color"])
# print(alien["points"])
# new_points = alien["points"]
# print("You just earned " + str(new_points) + " points")
# alien["x_position"] = 0
# alien["y_position"] = 25
# print(alien)
# alien = {}
# alien["color"] = "blue"
# alien["points"] = 5
# print(alien)
# alien["color"] = "green"
# print(alien)
# alien["test"] = 1
# print(alien)
# del alien["test"]
# print(alien)
favourite_languages = {
    "zhao":"python",
    "qian":"java",
    "sun":"c",
    "li":"c++"
    }
print("zhao's favourite language is " + favourite_languages["zhao"].title() + ".")
