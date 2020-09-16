#!/bin/bash
# Author:mochacha
# 日期：2020年9月15日
# 脚本说明：测试apk启动时间(冷启动/热启动)

# 安装apk，传入参数：apk文件的绝对地址
apk_install(){
    adb install -r $1
    sleep 5s
    # adb shell input keyevent 3
}

# 卸载apk，传入参数：apk包名
apk_uninstall(){
    adb uninstall $1
    sleep 5s
}

# 获取启动时间，传入参数：<apk包名>/<启动页活动名>
getStartupTime(){
    # grep -i 检索字符，sed -d 删除制表符，cut -d 截取字符串
    adb shell am start -W $1 | grep -i total | sed 's/ //g' | tr -d '\r' | cut -d ':' -f 2
    sleep 5s
}

# 清除应用所有进程，传入参数：apk包名
clearApp(){
    adb shell am force-stop $1
    sleep 5s
}

# 点击back按钮退出应用
quitApp(){
    adb shell input keyevent 3
    # adb shell input keyevent 4
    # adb shell input keyevent 4
    sleep 5s
}

read -p "请输入apk地址：" apk_address
read -p "请输入包名和活动名：" component
package_name=$(echo ${component} | cut -d "/" -f 1)
echo "apk包名为：${package_name}"
apk_uninstall $package_name

# 获取首次安装的启动时间，重复3次，最后取平均值
apk_install ${apk_address}
start_time1=$(getStartupTime ${component})
apk_uninstall $package_name

apk_install ${apk_address}
start_time2=$(getStartupTime ${component})
apk_uninstall $package_name

apk_install ${apk_address}
start_time3=$(getStartupTime ${component})
sleep 10s

echo "首次安装启动时间（ms）：$start_time1 $start_time2 $start_time3"
echo -n "平均启动时间（ms）："
echo "($start_time1+$start_time2+$start_time3)/3" | bc

# 获取热启动的启动时间，重复3次，最后取平均值
quitApp
start_time1=$(getStartupTime ${component})

quitApp
start_time2=$(getStartupTime ${component})

quitApp
start_time3=$(getStartupTime ${component})

echo "热启动时间（ms）：$start_time1 $start_time2 $start_time3"
echo -n "平均启动时间（ms）："
echo "($start_time1+$start_time2+$start_time3)/3" | bc

# 获取冷启动的启动时间，重复3次，最后取平均值
clearApp ${package_name}
start_time1=$(getStartupTime ${component})

clearApp ${package_name}
start_time2=$(getStartupTime ${component})

clearApp ${package_name}
start_time3=$(getStartupTime ${component})

echo "冷启动时间（ms）：$start_time1 $start_time2 $start_time3"
echo -n "平均启动时间（ms）："
echo "($start_time1+$start_time2+$start_time3)/3" | bc

# 测试结束，卸载app
apk_uninstall ${package_name}
