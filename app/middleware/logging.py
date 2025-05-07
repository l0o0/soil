import time
from fastapi import Request
from fastapi.responses import Response
import logging
from app.core.logger import setup_logging

# 初始化日志
logger = setup_logging()

async def logging_middleware(request: Request, call_next):
    # 记录请求开始
    start_time = time.time()
    client_ip = request.client.host if request.client else "unknown"
    
    # 记录请求信息
    extra = {
        "client_ip": client_ip,
        "method": request.method,
        "path": request.url.path,
        "status_code": "started",
        "response_time": "0ms"
    }
    
    logger.info(
        "Request started",
        extra=extra
    )
    
    try:
        # 处理请求
        response = await call_next(request)
    except Exception as e:
        # 记录异常信息
        extra.update({
            "status_code": "500",
            "response_time": f"{int((time.time() - start_time)*1000)}ms"
        })
        logger.error(
            f"Request failed: {str(e)}",
            exc_info=True,
            extra=extra
        )
        raise
    
    # 计算处理时间
    process_time = (time.time() - start_time) * 1000
    response_time = f"{int(process_time)}ms"
    
    # 记录请求完成
    extra.update({
        "status_code": response.status_code,
        "response_time": response_time
    })
    logger.info(
        "Request completed",
        extra=extra
    )
    
    # 添加响应头
    response.headers["X-Response-Time"] = response_time
    return response
