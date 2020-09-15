#!/bin/bash
# Author:mochacha
# 日期：2020年9月14日shell脚本练习

<<q
array=(1 2 3 4 5)
echo ${array[1]} //bash数组下标从1开始，zsh数组下标从0开始
for file in $(ls /Users); do 
    echo $file
done
q
printf "%d %s %f\n" //%d表示整数，%s表示字符串，%f表示浮点数
# 判断全部字符串相等
deive="device"
device_2=`adb devices`/$(adb devices)
if [[ $device_2 == *$device ]]; then
    echo "设备连接成功"
else
    "设备连接失败"
fi
# 执行算数运算的两种方法
1、$[2+3]
2、`expr 2 + 3` //此处必须有空格分隔开
# 执行脚本命令的两种方法
1、 $(adb devices)
2、`adb devices`
# $10不能获取第10个参数，第10个参数及之后需要${10..}
# 在数组内存储内容并输出
var=0
for i in $(ls /Users/apple/Desktop); do
    let var+=1
    array[$var]=$i
    echo $array[$var]
done