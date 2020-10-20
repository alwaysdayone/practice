# coding=utf-8
# author=mochacha

import json

# filename保存的是用户的图片数据（"data":{"work":[...这一段数据...]}）
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

for id in id_list:
    if id_list.count(id) > 1:
        print(id)