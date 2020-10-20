# coding=utf-8
# author=mochacha

# 方法一
# import json
# from collections import Counter

# filename = "/Users/apple/Desktop/yinwu.json"
# with open(filename) as get_user_data:
#     data = json.load(get_user_data)

# index = 0
# id_list = []
# while index < len(data):
#     paint_dicts = data[index]["paint"]
#     id = paint_dicts["id"]
#     id_list.append(id)
#     index += 1
    
# result = Counter(id_list)
# print(result)

# 方法二
import json

filename = "/Users/apple/Desktop/yinwu.json"
with open(filename) as get_user_data:
    data = json.load(get_user_data)

index = 0
id_list = []
while index < len(data):
    paint_dicts = data[index]["paint"]
    id = paint_dicts["id"]
    id_list.append(id)
    index += 1

# id_data = "\n".join(id_list)
for id in id_list:
    # print("%s 出现的次数：%d"%(id, id_list.count(id)))
    if id_list.count(id) > 1:
        print(id)