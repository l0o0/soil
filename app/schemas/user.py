from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str
    phone: str

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: Optional[bool] = True