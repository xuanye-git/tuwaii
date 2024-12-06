FROM python:3.9-slim

# 安装依赖
RUN apt-get update && apt-get install -y wget unzip
RUN pip install selenium

# 拷贝项目文件
COPY . /app
WORKDIR /app

# 运行测试
CMD ["python", "-m", "src.tests.test_game"]
