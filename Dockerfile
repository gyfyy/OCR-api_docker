# 使用官方 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 将当前目录的所有文件复制到容器的 /app 目录
COPY . /app

# 安装任何需要的依赖（如果有的话）
# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt


# 启动 Python 脚本
CMD ["python", "main.py"]
