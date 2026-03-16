#!/bin/bash

echo "==== 启动无人公司系统 ===="
echo "1. 启动数据库与基础服务"
cd ~/ai-company || exit
docker compose up -d

echo "2. 激活虚拟环境"
source .venv/bin/activate

echo "3. 启动 FastAPI 指挥中心"
uvicorn main:app --reload --host 127.0.0.1 --port 8001
