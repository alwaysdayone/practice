# coding=utf-8
# author=mochacha

import json

# filename保存的是用户的json数据
filename = "/Users/apple/Desktop/1.json"
with open(filename) as get_user_data:
    data = json.load(get_user_data)

data_2 = data["data"]["work"]

index = 0
id_list = []
while index < len(data_2):
    paint_dicts = data_2[index]["paint"]
    id = paint_dicts["id"]
    id_list.append(id)
    index += 1

for id in id_list:
    if id_list.count(id) > 1:
        print(id)