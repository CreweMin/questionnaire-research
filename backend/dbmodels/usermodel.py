from sqlalchemy import Column, String, Integer
from orml.dbbase import Base
from conf import table_args


class User(Base):
    __table_args__ = table_args
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20))
    user_password = Column(String(100))
    user_role_id = Column(Integer)
    
