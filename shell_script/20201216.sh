#!/bin/bash
# author:mochacha
# date:20201216

# echo "test by mochacha"
# name="liu xuyang"
# echo $name
# echo `ls`
# echo $(ls)
# name="liu xuyang"
# # readonly name
# echo $name
# # echo ${name}
# # 删除变量
# unset name
# echo $name
# your_name="runoob"
# str="Hello, I know you are $your_name!"
# str="Hello, I know you are "$your_name"!"
# echo $str
# echo -e $str
# echo ${#str}
# echo ${str:1:4}
# echo `expr index "$str" on`
array_name=(1 2 3333 4 5)
# echo ${array_name[1]}
# echo ${array_name[@]}
:<<a
length=${#array_name[@]}
echo $length
length=${#array_name[*]}
echo $length
length=${#array_name[2]}
echo $length
a
:<<,
echo "shell传递参数事例"
echo "执行的文件名为：$0"
echo "第一个参数为：$1"
echo "第二个参数为：$2"
echo "第三个参数为：$3"
echo "传递到脚本的参数个数为：$#"
echo "向脚本传递的参数依次为：$*"
echo "向脚本传递的参数依次为：$@"
echo "显示最后命令的退出状态：$?"
for i in "$*"; do echo $i; done
for j in "$@"; do echo $j; done
,
# result=`expr 2 + 2`
# echo $result
# result=$[2+2]
# echo $result
# result=$(ls)
# echo $result
# result=`ls`
# echo $result
# result=`expr 2 \* 3`
# a=$result
# echo $result
# echo $a
# if [ $result == $a ]; then echo "相等"; fi
# result=`expr 2 + 2`
# echo $result
# result=$[2+2]
# echo $result
# result=$[2 + 2]
# echo $result
# result=$((2+2))
# echo $result
# a=10
# b=20
# if [[ $a -lt 100 && $b -lt 100 ]]; then echo "true"; fi
# read -p "请输入你的名字：" name
# echo $name
# read name
# echo "$name It is a test"
# -e 开启转义功能
# echo -e "OK\n"
# -c 开启不换行功能
# echo -e "OK \c"
# echo "It is a test"
# echo `date`
# echo $(date)
# echo "Hello, Shell"
# printf "Hello, Shell"
# printf "Hello Shell\n"
# printf "%-10s %-8s %4s\n" 姓名 性别 体重kg
# printf "%-10s %-8s %4.2f\n" 刘阳 男 76.125
printf "%s and %d\n" str 123