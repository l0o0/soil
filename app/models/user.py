from sqlalchemy import Column, String, Integer, Boolean
from app.models import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    phone = Column(String(20), unique=True)
    hashed_password = Column(String(300))
    is_active = Column(Boolean, default=True)
    
    # 预留扩展字段
    class Config:
        from_attributes = True