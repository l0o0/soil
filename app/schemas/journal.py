from datetime import datetime
from pydantic import BaseModel
from typing import Dict, Optional, Union


class CNKICreate(BaseModel):
    """
    CNKI 论文数据创建模型
    """
    qkmc: str
    fhyz: Optional[float] = None
    zhyz: Optional[float] = None
    pyear: Optional[int] = None

class CNKIUpdate(BaseModel):
    """
    CNKI 论文数据更新模型
    """
    fhyz: Optional[float] = None
    zhyz: Optional[float] = None
    pyear: Optional[int] = None

class CNKIResponse(BaseModel):
    """
    CNKI 论文数据响应模型
    """
    qkmc: str
    fhyz: Optional[float] = None
    zhyz: Optional[float] = None
    pyear: Optional[int] = None
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None

class JournalResponse(BaseModel):
    name: str
    data: Optional[Dict[str, Union[str, float]]] = None