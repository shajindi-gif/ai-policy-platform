#!/bin/bash

echo "==== 停止无人公司系统 ===="
pkill -f "uvicorn main:app"
cd ~/ai-company || exit
docker compose down
