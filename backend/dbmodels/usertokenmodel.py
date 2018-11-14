from sqlalchemy import Column, String, Integer
from orml.dbbase import Base
from conf import table_args


class Usertoken(Base):
    __table_args__ = table_args
    __tablename__ = 'usertoken'
    user_token = Column(String(100),primary_key=True)
    user_id = Column(Integer)
