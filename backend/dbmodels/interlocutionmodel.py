from sqlalchemy import Column, String, Integer
from orml.dbbase import Base
from conf import table_args


class Interlocution(Base):
    __table_args__ = table_args
    __tablename__ = 'interlocution'
    interlocution_id = Column(Integer, primary_key=True)
    interlocution_subject_id = Column(Integer)
    interlocution_content = Column(String(300))
