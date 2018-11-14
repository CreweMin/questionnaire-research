from sqlalchemy import Column, String, Integer,Float
from orml.dbbase import Base
from conf import table_args


class Optiontable(Base):
    __table_args__ = table_args
    __tablename__ = 'optiontable'
    option_id = Column(Integer, primary_key=True)
    option_subject_id = Column(Integer)
    option_content = Column(String(50))
    option_total = Column(Integer)
    option_percent = Column(Float)
