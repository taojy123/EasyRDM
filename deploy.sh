#!/bin/sh

echo "pull"
docker pull registry.cn-shanghai.aliyuncs.com/taojy123/easyrdm

echo "stop"
docker stop easyrdm

echo "run"
sleep 1
docker run --name easyrdm -p 6007:8080 -d --rm registry.cn-shanghai.aliyuncs.com/taojy123/easyrdm

echo "finish"
sleep 1
docker ps -a

