#!/bin/bash
# Author:mochacha
# 日期：2020年9月14日
# 脚本说明：Android apk包脚本工具

# 安装app
letu_install(){
    echo -n "请输入apk地址："
    read apk_path
    adb install -r $apk_path
}

# 卸载乐涂app
letu_uninstall(){
    adb uninstall paint.by.number.pixel.art.coloring.drawing.puzzle
}

# 卸载KJVapp
kjv_uninstall(){
    adb uninstall kjv.bible.kingjamesbible
}

# 查看包名/活动名
cat_package(){
    adb shell "dumpsys window w|grep \/|grep name=|sed 's/mSurface=Surface(name=//g'|sed 's/)//g'|sed 's/ //g'"
}

# 截图操作
screencap(){
    adb shell screencap -p /sdcard/$filename.png
}

# 导出截图
pull_screencap(){
    if (! -d "screencap"); then
        mkdir screencap
    fi
    adb pull /sdcard/$filename.png $path/screencap
}

# 录屏操作
screenrecord(){
    echo -n "请输入录制时间（s）："
    read second
    adb shell screenrecord --time-limit $second /sdcard/$filename_2.mp4
}

# 导出录屏
pull_screenrecord(){
    if (! -d "screenrecord"); then
        mkdir screenrecord
    fi
    adb pull /sdcard/$filename_2.mp4 $path/screenrecord
}

dev="device"
device=`adb devices`
if [[ $device == *$dev ]]; then
    echo "设备连接成功，请选择你要进行的操作："
    printf "%-12s %-12s %-12s %-12s\n" 安装app：输入1 卸载乐涂：输入2 卸载KJV：输入3 查看包名/活动名：输入4
    printf "%-12s %-12s %-12s %-12s\n" 截图操作：输入5 导出截图：输入6 录屏操作：输入7 导出录屏：输入8
    printf "%-12s\n\n" 退出操作：输入任意字符
    filename=1
    filename_2=1
    path=$(pwd)
    while true; do
        echo -n "请输入："
        read number
        case $number in
            1)letu_install;;
            2)letu_uninstall;;
            3)kjv_uninstall;;
            4)cat_package;;
            5)screencap;;
            6)pull_screencap
            let filename++;;
            7)screenrecord;;
            8)pull_screenrecord
            let filename_2++;;
            *)break;;
        esac
    done
else
    echo "设备连接失败，请检查设备后重试"
fi