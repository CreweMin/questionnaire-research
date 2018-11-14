from sqlalchemy import Column, String, Integer
from orml.dbbase import Base
from conf import table_args

class Role(Base):
    __table_args__ = table_args
    __tablename__ = 'role'
    role_id = Column(Integer, primary_key=True)
    role_content = Column(String(10))
