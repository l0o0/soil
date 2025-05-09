from typing import Union
from fastapi import HTTPException, Header
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from app.core.config import settings

id_list = settings.PLUGIN_IDS.split(",") if settings.PLUGIN_IDS else []

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ENCRYPT_ALGORITHM)
    return encoded_jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# 只限制部分插件ID能使用
async def verify_pluginID(pluginID: str = Header(...)):
    """
    验证请求头中的pluginID是否有效
    """
    print(id_list, pluginID)
    if pluginID not in id_list:
        raise HTTPException(
            status_code=401,
            detail="Invalid plugin ID",
        )
