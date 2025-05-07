import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
import os

def setup_logging():
    # 获取当前项目根目录
    project_root = Path(__file__).parent.parent.parent
    # 创建相对路径的日志目录
    log_dir = project_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # 主日志文件路径
    log_file = log_dir / "fastapi.log"
    
    # 创建日志格式
    log_format = (
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s - "
        "IP: %(client_ip)s - Method: %(method)s - Path: %(path)s - "
        "Status: %(status_code)s - ResponseTime: %(response_time)s"
    )
    formatter = logging.Formatter(log_format)
    
    # 创建文件日志处理器
    file_handler = TimedRotatingFileHandler(
        filename=log_file,
        when="W0",        # 每周一凌晨轮换
        interval=1,       # 每周
        backupCount=12,   # 保留12个备份
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    # 创建控制台日志处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)
    
    # 配置根日志
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

class RequestLogFilter(logging.Filter):
    """添加请求上下文到日志记录"""
    def filter(self, record):
        # 设置默认值
        record.client_ip = getattr(record, 'client_ip', 'unknown')
        record.method = getattr(record, 'method', 'unknown')
        record.path = getattr(record, 'path', 'unknown')
        record.status_code = getattr(record, 'status_code', 'unknown')
        record.response_time = getattr(record, 'response_time', 'unknown')
        return True
