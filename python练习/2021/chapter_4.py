# coding = utf-8
# author = mochacha
# 2021年4月19日

# import datetime
# import time

# 操作列表
# 列表解析
# squares = [value ** 2 for value in range(1,11)]
# print(squares)
# Q1
# for number in range(1, 21):
#     print(number, end=" ")
# Q2
# for number in range(1, 1000001):
#     print(number, end=" ")
# Q3
# number_list = list(range(1, 1000001))
# print(max(number_list))
# print(min(number_list))
# print(sum(number_list))
# 计算1-1000000的和及计算时间
# start_time = datetime.datetime.now()
# print(sum(range(1, 1000001)))
# end_time = datetime.datetime.now()
# print(end_time - start_time)

# start_time = time.time()
# print(sum(range(1, 1000001)))
# end_time = time.time()
# print(end_time - start_time)
# Q4
# for number in range(1, 21, 2):
#     print(number, end=" ")
# Q4
# for number in range(3, 31):
#     if number % 3 == 0:
#         print(number, end=" ")
# Q5
# squares = []
# number_list = list(range(1, 11))
# for number in number_list:
#     square = number ** 3
#     squares.append(square)
# print(squares)
# Q6
# print([number ** 3 for number in range(1, 11)])

# 列表切片
# number_list = list(range(1, 11))
# print(number_list[0:3])
# print(number_list[:3])
# print(number_list[3:12])
# print(number_list[3:])
# print(number_list[-3:])
# list_1 = [1,2,3,4]
# list_1.reverse()
# print(list_1)

# list_1 = [1,2,3,4]
# print(list(reversed(list_1)))

# list_1 = [1,2,3,4]
# list_1.sort(reverse=True)
# print(list_1)

# list_1 = [1,2,3,4]
# print(sorted(list_1, reverse=True))

# list_1 = [1,2,3,4]
# print(list_1[::-1])
# 复制列表
# car = [1,2,3,4]
# my_car = car[:]
# print(car)
# print(my_car)
# car.insert(4, 5)
# my_car.append(6)
# print(car)
# print(my_car)

# 元组
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
# dimensions[0] = 250
# for dimension in dimensions:
#     print(dimension, end=" ")
# dimensions = (400, 100)
# print('\n')
# for dimension in dimensions:
#     print(dimension, end=' ')
# dimensions_2 = list(dimensions)
# print(dimensions_2)
# dimensions_2[0] = 500
# dimensions = tuple(dimensions_2)
# for dimension in dimensions:
#     print(dimension)
