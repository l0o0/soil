# Soil

## 1. 项目结构

项目目录结构：
```
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
```

## 2. 运行项目
启动数据库

```
docker start postgresql
```

以 docker 容器运行项目
将配置文件和日志目录挂载到容器中，同时注意此时的环境变量`ENV`设置为 prod。

```
cd soil
docker build -t soil .
docker run -d -e ENV=prod -v $(pwd)/.env.prod:/app/.env.prod -v $(pwd)/logs:/app/logs -p 8080:8080 --name soil
```

## 3. API 文档

### 3.1 期刊缩写
```javascript
const journalName = "2D Materials";
resp = await Zotero.HTTP.request(
    "GET", 
    `http://host-name/v1/journals/abbreviation/${encodeURI(journalName)}`, 
    {headers: {pluginID: "plugin-addon-ID"}}
);
JSON.parse(resp.responseText);
// {"name":"2D Materials","data":{"abb_with_dot":"2D Mater.","abb_no_dot":"None"}}
// return {"name":"AAAAA","data":null}  when no abbreviation found.
```

### 3.2 中国知网复合影响因子和综合影响因子
```javascript
const journalName = "园艺学报";
resp = await Zotero.HTTP.request(
    "GET", 
    `http://host-name/v1/journals/cnki/${encodeURI(journalName)}`, 
    {headers: {pluginID: "plugin-addon-ID"}}
);
JSON.parse(resp.responseText);
// {"name":"园艺学报","data":{"fhyz":"3.0440","zhyz":"2.3920"}}
// return {"name":"AAAAA","data":null}  when no data found.
```

## 4. 压力测试

1. 压测工具：Python locust
2. 压测脚本：`test/locust/locustTest.py`
3. 操作步骤

`uv run --group dev locust -f test/locust/locustTest.py`

打开浏览器访问 http://localhost:8089。

输入以下参数：
    Number of users：模拟用户数（如 100）。
    Spawn rate：每秒启动的用户数（如 10）。
    Host：http://127.0.0.1:8000。



