#!/bin/sh

if [ $# -eq 0 ];then
    exit
else
    a=$*
    if [ $a = "build" ]; then
        docker build -t eric/githook .
        exit
    elif [ $a = "dev" ]; then
        docker-compose stop dev
        docker-compose up -d dev
        docker exec -it githook_dev_1 bash
        exit
    elif [ $a = "pro" ]; then
        docker-compose stop pro
        docker-compose up -d pro
        exit
    elif [ $a = "rls" ]; then
        docker-compose stop rls
        docker-compose up -d rls
        exit
    fi
fi