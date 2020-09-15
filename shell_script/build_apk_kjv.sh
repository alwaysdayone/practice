#!/bin/bash
# Author:mochacha
# 日期：2020年9月15日
# 脚本说明：kjv Android打包脚本

:<<EOF
脚本说明：
执行 ./build_apk.sh 命令打debug包
执行 ./build_apk release命令打release包
EOF

build_debug(){
    rm -rf $scr_debug_path
    if [ -d debugApk ]; then
        rm -rf $root_path/debugApk/*
    elif [ ! -d debugApk ]; then
        mkdir debugApk
    fi
    echo "开始打debug包..."
    ./gradlew assembleDebug
    cp $scr_debug_path $root_path/debugApk
    open $root_path/debugApk
    echo "debug包打好了亲，请在debugApk文件夹下查看～"
}

build_release(){
    rm -rf $scr_release_path
    if [ -d releaseApk ]; then
        rm -rf $root_path/releaseApk/*
    elif [ ! -d releaseApk ]; then
        mkdir releaseApk
    fi
    echo "开始打release包..."
    ./gradlew assembleRelease
    cp $scr_release_path $root_path/releaseApk
    cp $scr_mapping_path $root_path/releaseApk
    open $root_path/releaseApk
    echo "release包打好了亲，请在releaseApk文件夹下查看～"
}

root_path=$(pwd)
scr_debug_path=$root_path/alkitab/build/outputs/apk/production/debug/*
scr_release_path=$root_path/alkitab/build/outputs/apk/production/release/*
scr_mapping_path=$root_path/alkitab/build/outputs/mapping/production/release/mapping.txt

if [[ $1 == "release" ]]; then
    build_release
else
    build_debug
fi