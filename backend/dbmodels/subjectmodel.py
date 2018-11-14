from sqlalchemy import Column, String, Integer
from orml.dbbase import Base
from conf import table_args


class Subject(Base):
    __table_args__ = table_args
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String(200))
    subject_option_flag = Column(Integer)
    subject_questionnaire_id = Column(Integer)
    
