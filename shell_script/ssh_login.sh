#!/bin/bash
# Author=mochacha
# 日期：2020年9月13日
# 脚本说明：在linux环境下通过ssh登录服务器，结合alias使用比较方便

# 方法一
set host "xxx.xxx.xxx.xxx"
set password "xxxxxx"
spawn ssh ec2-user@$host
expect{
    "yes/no"{send "yes"\r, exp_continue};
    "password"{send "$password\r"}
}
interact
# expect eof

# 方法二
set host "xxx.xxx.xxx.xxx"
set password "xxxxxx"
spawn ssh ec2-user@$host
expect "yes/no"
send "yes\n"
expect "password"
send "$password"
expect eof

