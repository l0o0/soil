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

