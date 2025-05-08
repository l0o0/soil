# Soil



项目目录结构：

app

    main.py  主入口程序
    routers API路由，分版本v1，v2
    config  配置文件
    db       数据库
    models  数据库模型
    schemas 数据模型
    services 业务逻辑
    test
    utils
.env    环境变量配置文件
alembic 数据库迁移工具目录
Dockerfile
README.md

## 启动数据库

docker start postgresql

## 运行项目

以 docker 容器运行项目
将配置文件和日志目录挂载到容器中，同时注意此时的环境变量 ENV 设置为 prod。

```
docker build -t soil .
docker run -d -e ENV=prod -v $(pwd)/.env.prod:/app/.env.prod -v $(pwd)/logs:/app/logs -p 8080:8080 --name soil
```



## 压力测试

1. 压测工具：Python locust
2. 压测脚本：`test/locust/locustTest.py`
3. 操作步骤

`uv run --group dev locust -f test/locust/locustTest.py`

打开浏览器访问 http://localhost:8089。

输入以下参数：
    Number of users：模拟用户数（如 100）。
    Spawn rate：每秒启动的用户数（如 10）。
    Host：http://127.0.0.1:8000。



