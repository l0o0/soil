# 阶段1:构建依赖
FROM python:3.12-slim as builder

# 1. 安装 uv (比 pip 快 10-100 倍)
RUN pip install --no-cache-dir uv -i https://pypi.tuna.tsinghua.edu.cn/simple

# 设置工作目录
WORKDIR /app
COPY pyproject.toml .

# 3. 使用 uv sync 直接安装依赖到系统路径 (不生成 requirements.txt)
RUN uv pip install --system --no-cache .

# ----------------------------
# 阶段2: 生产镜像
FROM python:3.12-slim

# 1. 从构建阶段复制已安装的依赖
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 2. 复制应用代码
WORKDIR /app
COPY . .

EXPOSE 8000
# 3. 设置环境变量
ENV ENV=prod

# 3. 启动应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
