# coding = utf-8
# author = mochacha
# date = 2020.12.14

file_path = "/Users/apple/Documents/lxsw_project/practice/test_files/pi_digits.txt"
# test_file = open(file_path)
# print(test_file.read().strip())
# test_file.close()
# with open(file_path) as test_file:
#     content = test_file.read().strip()
#     print(content)
# with open(file_path) as test_file:
#     for line in test_file:
#         print(line.rstrip())
# with open(file_path) as test_file:
#     lines = test_file.readlines()
    
# pi_string = ""
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(pi_string[:10])
# print(len(pi_string))
# with open(file_path, 'a+') as test_file:
#     test_file.write("test by mochacha.\n")
    
# with open(file_path, 'r') as test_file_2:
#     content = test_file_2.read().strip()
#     print(content)
# try:
#     print(5/0)
# except:
#     print("被除数不能为0！")
# print("Give me two numbers, and I'll divide them")
# print("Enter 'q' to quit the program")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     secend_number = input("\nSecend number: ")
#     if secend_number == 'q':
#         break
#     try:
#         result = int(first_number)/int(secend_number)
#     except:
#         print("被除数不能为0， 请重新输入！")
#     else:
#         print("结果为: " + str(result))

# file_name = "test.txt"
# try:
#     with open(file_name) as test_file:
#         content = test_file.read().strip()
# except:
#     print("文件不存在！")
# else:
#     print(content)
# text = 'alice, in wonderlang'
# list1 = text.split(',')
# print(list1)

# a = lambda x:x+2
# print(a(2))