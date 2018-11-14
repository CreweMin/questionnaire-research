from sqlalchemy import Column, String, Integer,Date
from orml.dbbase import Base
from conf import table_args


class Searchlog(Base):
    __table_args__ = table_args
    __tablename__ = 'searchlog'
    searchlog_id = Column(Integer, primary_key=True)
    searchlog_userid = Column(Integer)
    searchlog_keywords = Column(String(20))
    searchlog_datetime = Column(Date)
