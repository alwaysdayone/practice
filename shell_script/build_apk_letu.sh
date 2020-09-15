#!/bin/bash
# Author:mochacha
# 日期：2020年9月15日
# 脚本说明：乐涂 Android打包脚本

GREEN_COLOR="\033[32m"
# thinker删除旧基准包逻辑
echo -e "$GREEN_COLOR\n重新生成基准包前，删除上一次的基准包"
bakApk_path=app/build/bakApk
bakApk_channel_path=app/build/bakApk/falvar
if [ -d $bakApk_path ]; then
    rm -rf $bakApk_path
    echo -e "$GREEN_COLOR\n基准包删除成功，开始打包流程..."
else
    echo -e "$GREEN_COLOR\n未找到上次的基准包，直接开始打包..."
fi

# 重命名基准包文件夹名字
renameBakApk(){
    for file in `ls $bakApk_channel_path`; do
    if [[ $file =~ $1 ]]; then
        mv $bakApk_channel_path/$file $bakApk_channel_path/$1
        echo -e "$GREEN_COLOE\n $1基准包重命名成功"
        break
    fi
    done
}

is_open_dir=true
is_offline_work=true

# debug / release
configuration=debug
# 支持渠道 baidu_organic toutiao toutiao_letu other
# other渠道包括：vivo、oppo、hauwei、yingyongbao、xiaomi、cn360、ali、kuaishou、guangdiantong、baidu
channels=()

if [ $# -gt 0]; then
    index=0
    for i in "$@"; do
        if [ $i == debug ]; then configuration=$i; continue; fi
        if [ $i == release ]; then configuration=$i; continue; fi
        if [ $i == close_dir ]; then is_open_dir=false; continue; fi
        if [ $i == offline ]; then is_offline_work=true; continue; fi
        if [ $i == online ]; then is_offline_work=false; continue; fi
        if [ $i == all ]; then continue; fi
        channels[$index]=$i
        let index++
    done
fi

if [ ! -d app/build/outputs/apks ]; then
    mkdir app/build/outputs/apks
fi

output_dir=app/build/outputs/apks/$configuration
output_dir_toutiao=app/build/outputs/apks/$configuration/头条数字填色
output_dir_toutiao_letu=app/build/outputs/apks/$configuration/头条乐涂数字填色
if [ ${#channels[*]} -eq 0 ]; then
    channels=(other toutiao baidu_organic toutiao_letu)
fi

echo -e "$GREEN_COLOR\n 开始打包：$configuration 渠道个数：${#channels[*]}"
rm -rf $output_dir
mkdir $output_dir

for((i=0;i<${#channels[*];i++})); do
    channel=${channels[i]}
    cp app/channels/channel_$channel app/build/channel
    rm -rf app/build/outputs/channels
    echo -e "$GREEN_COLOR\n 开始打包渠道：$channel\n"
    if [ $is_offline_work == true ]; then
        ./gradlew assemble${channel}${configuration}channels --offline
    else
        ./gradlew assemble${channel}${configuration}channels
    fi
    renameBakApk $channel
    if [[ $channel == toutiao ]]; then
        cp -r app/build/outputs/channels/ $output_dir_toutiao
    elif [[ $channel == toutiao_letu ]]; then
        cp -r app/build/outputs/channels/ $output_dir_toutiao_letu
        rename 's/toutiao/toutiao_letu' $output_dir_toutiao_letu/*
    else
        cp -r app/build/outputs/channels/ $output_dir
    fi
    echo -e "$GREEN_COLOR\n 完成打包渠道：$channel\n"
done

echo -e "$GREEN_COLOR\n 恭喜你，所有渠道打包完成！！！\n输出文件夹为：$output_dir\n"

if [ $is_open_dir == true ]: then
    open $output_dir
fi
