from sqlalchemy import Column, String, Integer
from orml.dbbase import Base
from conf import table_args


class Classify(Base):
    __table_args__ = table_args
    __tablename__ = 'classify'
    classify_id = Column(Integer, primary_key=True)
    classify_content = Column(String(20))
