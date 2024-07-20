#!/bin/bash

# 终止8000端口的所有进程
lsof -i :8008 | grep LISTEN | awk '{print $2}' | xargs -r kill -9

# 设置PYTHONPATH变量为当前目录
export PYTHONPATH=$(pwd)

# 递归清除当前目录及子目录下的__pycache__目录
find . -type d -name '__pycache__' -exec rm -r {} +

# 调用python api.py
python api.py