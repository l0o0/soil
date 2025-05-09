from sqlalchemy import Column, Integer, String, Numeric, SmallInteger, DateTime, func
from app.models import Base

class CNKIM(Base):
    """
    CNKI论文数据表模型
    对应PostgreSQL中的public.cnki表
    """
    __tablename__ = 'cnki'
    __table_args__ = {'schema': 'public'}
    
    # 主键字段
    qkmc = Column(String(100), primary_key=True, nullable=False, comment='期刊名称')
    
    # 数值字段
    fhyz = Column(Numeric(7, 4), nullable=True, comment='复合影响因子')
    zhyz = Column(Numeric(7, 4), nullable=True, comment='综合影响因子')
    
    # 时间字段
    pyear = Column(SmallInteger, nullable=True, comment='出版年份')
    create_time = Column(DateTime(timezone=True), nullable=True, default=func.now(), comment='创建时间')
    update_time = Column(DateTime(timezone=True), nullable=True, onupdate=func.now(), comment='更新时间')
    
    def __repr__(self):
        return f"<CNKI(qkmc='{self.qkmc}',fhyz='{self.fhyz}', zhyz='{self.zhyz}', pyear={self.pyear})>"
    

class AbbreviationM(Base):
    """
    Journal abbreviation model
    期刊缩写
    """
    __tablename__ = "abbreviation"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(255), index=True)
    abb_with_dot = Column(String(255))
    abb_no_dot = Column(String(255))