#!/bin/bash
# Author:mochacha
# 日期：2020年9月7日shell脚本练习

# echo "Test"
# name=liuxuyang
# echo $name
# for file in `ls /Users/apple/Desktop`; do
#     echo $file
# done
# for file in $(ls /Users/apple/Desktop)
# do
#     echo "This is $file"
# done
# name="test"
# # echo $name
# # # name="test1"
# # # echo $name
# # unset name
# # echo $name
# # echo 'this is a test $name'
# # -e输出识别转义字符
# echo -e "this is a test "$name"! \n" 
# str="abcd"
# echo ${str:1:2}
#多行注释，:<<+任意字符
:<<a
array=(a b c d e)
array_2=(
    value1
    value2
    value3
)
array_3[0]=value1
array_3[1]=value2
array_3[4]=value3
# echo ${array[2]}
# echo ${array[@]}
echo ${#array[@]}
echo ${#array_2[*]}
echo ${#array_3[1]}
a
:<<a
echo "传递参数实例"
echo "执行的文件名为：$0"
echo "第一个参数为：$1"
echo "第二个参数为：$2"
echo "第三个参数为：$3"
echo "参数的个数为：$#"
echo "传递的参数为：$*"
echo "传递的参数为：$@"
for i in "$*"; do
    echo $i
done
for j in "$@"; do
    echo $j
done
a
# val=`expr 2 + 2`
# echo $val
# val2=$[2+2]
# echo $val2
# val3=$[3%2]
# echo $val3
:<<a
a=10
b=20
if [ $a == $b ]; then
    echo "a等于b"
else
    echo "a不等于b"
fi
if [ $a != $b ]; then
    echo "a"
else
    echo "b"
fi

a=10
b=20
if [ $a -eq $b ]; then
    echo "a=b"
else
    echo "a!=b"
fi
if [ $a -ne $b ]
if [ $a -gt $b ]
if [ $a -lt $b ]
if [ $a -ge $b ]
if [ $a -le $b ]
if [ $a -gt $b -o $a -le $b ]
if [[ $a -gt 100 && $a -lt 10 ]]
if [[ $a -eq 100 || $a -ne 10 ]]
if [ $a = $b ]
if [ $a != $b ]
if [ -z $b ]
if [ -n $b ]
if [ $b ]; then
    echo ""

file="/Users/apple/Desktop/test.txt"
if [ -e $file ]; then
    echo "file是普通文件"
else
    echo "file不是普通文件"
fi
a
# echo "It is a test"
# echo "\"It is a test\""
# echo -n "请输入您的名字："
# read name
# echo "I'm $name"
# echo -e "OK \c"
# echo "test"
# echo "test" > outfile.txt
# echo < outfile.txt
# echo `date`
# echo $(date)
# echo "Hello"
# printf "Hello \n"
# printf "%-8s %-8s %-8s\n" 刘旭阳 男 80
:<<a
echo -n "请输入您的姓名："
read name
echo -n "请输入您的性别："
read sex
echo -n "请输入您的年龄："
read age
printf "%-8s %-8s %-8s\n" 姓名 性别 体重
printf "%-8s %-8s %-8s\n" $name $sex $age
printf '%d %s\n' 1 abc

# printf %s abc def
# printf "%s and %d"
num1=101
num2=100
if test $num1 = $num2; then
    echo "两个数相等"
else
    echo "两个数不相等"
fi
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi
if [ 1 -lt 0 ]; then
    echo "1"
elif [ 1 -gt 0 ]; then
    echo "2"
else
    echo "3"
fi

# for file in $(ls /Users/apple/Desktop); do
#     echo $file
# done
# int=1
# while (($int<=5)); do
#     echo $int
#     let int++
# done
# echo "按下 <Ctrl+D> 退出"
# echo -n "输入任意字符："
# while read var; do
#     echo "你输入的字符是：$var"
# done
# var=1
# while true; do
#     echo $var
#     let var++
# done
# a=0
# until [ $a -gt 10 ]; do
#     echo $a
#     a=$[a+1]
# done
echo "输入1-4之间的数字："
echo -n "你输入的数字为："
read num
case $num in
    1)echo "你选择了1";;
    2)echo "你选择了2";;
    3)echo "你选择了3";;
    4)echo "你选择了4";;
    *)echo "你没有选择1-4之间的数字";;
esac

while true; do
    echo -n "请输入1-5之间的数字："
    read num
    case $num in
        1|2|3|4|5)echo "你输入的数字是：$num";;
        *)echo "你输入的数字不在1-5之间！"
        # break;;
        continue
        echo "游戏结束!";;
    esac
done
a
# demo(){
#     echo "shell函数测试"
# }
# demo
# add_test(){
#     echo -n "输入第一个数字："
#     read num1
#     echo -n "输入第二个数字："
#     read num2
#     return $[$num1+$num2]
# }
# add_test
# echo $?
# . filename
# source filename
# 2>&1