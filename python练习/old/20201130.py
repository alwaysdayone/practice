# coding = utf-8
# author = mochacha
# date = 2020.11.30

# 列表
# car_list = ["benchi", "baoma", "Aodi", "test"]
# print(car_list)
# car_list.sort()
# print(car_list)
# car_list.sort(reverse=True)
# print(car_list)
# print(sorted(car_list, reverse=True))
# print(car_list)
# car_list.reverse()
# print(car_list)
# print(len(car_list))
# print(car_list[-1]) # -1可以固定打印列表中的最后一个元素
# for car in car_list:
#     print("汽车的名称为：" + car)
# print("测试结束")
# test = "test"
#     print(test)
# for car in car_list:
#     print(car)

# 1-100，求和
# number = 0
# for i in range(1, 101):
#     number = number + i
# print(number)

# print(sum(range(1, 101)))

# 使用range生成数字列表(首、尾、步长)
# numbers = list(range(1, 10, 3))
# print(numbers)

# squares = []
# for i in range(1, 11):
#     # square = i ** 2
#     # squares.append(square)
#     squares.append(i ** 2)
# print(squares)

# digits = list(range(1, 11))
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# 列表解析
# squares = [i ** 2 for i in range(1, 11)]
# print(squares)

# nums = list(range(1, 11))
# print(nums[1:3])
# print(nums[:4])
# print(nums[5:])
# print(nums[:])
# print(nums[-3:])
# for i in nums[2:5]:
#     print(i)
# nums_2 = nums[:]
# print(nums_2)
# nums.append(11)
# nums_2.append(99)
# print(nums)
# print(nums_2)

# 元组
# dimensions = (50 ,200)
# print(dimensions[0])
# print(dimensions[1])
# for dimension in dimensions:
#     print(dimension)
# 元组中的元素不可更改，但是可以修改整个元组
# dimensions = (100, 400)
# for dimension in dimensions:
#     print(dimension)

cars = ["audi", "bmw", "benchi"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car)