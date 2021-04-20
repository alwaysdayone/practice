#!/bin/bash
# 脚本说明：安装应用，计算平均冷启动/热启动时间
# 适用app：Bible Verse Connect
# 传入参数：1.apk文件的绝对地址 2.app包名/活动名

# apk安装，传入参数：apk文件的绝对地址
function install(){
    adb shell input keyevent 3
    adb install ${1}
    sleep 5s
}

# apk卸载，传入参数：apk应用包名
function uninstall(){
    adb uninstall ${1}
    sleep 2s
}

# 获取启动时间，传入参数：<包名>/<活动名>
function getStartUpTime(){
    # adb shell am start -W ${1} | grep -i total | tr -d '\r' | cut -d ':' -f 2
    adb shell am start -W ${1} | grep -i total | sed 's/ //g' | cut -d ':' -f 2
    sleep 2s
}

# 清除应用进程，传入参数：apk应用包名
function cleanApp(){
    adb shell am force-stop ${1}
    sleep 5s
}

# back键退出app
function quitApp(){
    adb shell input keyevent 4
    adb shell input tap 600 1800
    sleep 2s
}

# 运行脚本后，提示输入apk文件地址、包名/启动页活动名
read -p "请输入apk地址: " apk_address
read -p "请输入包名/活动名: " component

# 获取包名赋值给变量“package_name”
package_name=`echo ${component} | cut -d '/' -f 1`
echo "Package name is '${package_name}'"

# 获取首次安装的启动时间，重复三次取平均值
install ${apk_address}
startTime1=`getStartUpTime ${component}`
uninstall ${package_name}
install ${apk_address}
startTime2=`getStartUpTime ${component}`
uninstall ${package_name}
install ${apk_address}
startTime3=`getStartUpTime ${component}`
sleep 10s
# 三次启动时间
echo "首次安装启动时间（ms）: ${startTime1} ${startTime2} ${startTime3}"
# 平均启动时间
echo "(${startTime1}+${startTime2}+${startTime3})/3" | bc

# 首次安装启动时间测试结束，开始热启动时间测试，重复三次取平均值
quitApp
startTime1=`getStartUpTime ${component}`
quitApp
startTime2=`getStartUpTime ${component}`
quitApp
startTime3=`getStartUpTime ${component}`
# 三次启动时间
echo "热启动时间（ms）: ${startTime1} ${startTime2} ${startTime3}"
# 平均启动时间
echo "(${startTime1}+${startTime2}+${startTime3})/3" | bc

# 热启动时间测试结束，开始冷启动时间测试，重复三次取平均值
cleanApp ${package_name}
startTime1=`getStartUpTime ${component}`
cleanApp ${package_name}
startTime2=`getStartUpTime ${component}`
cleanApp ${package_name}
startTime3=`getStartUpTime ${component}`
# 三次启动时间
echo "冷启动时间（ms）: ${startTime1} ${startTime2} ${startTime3}"
# 平均启动时间
echo "(${startTime1}+${startTime2}+${startTime3})/3" | bc

# 启动时间测试结束，卸载app
uninstall ${package_name}