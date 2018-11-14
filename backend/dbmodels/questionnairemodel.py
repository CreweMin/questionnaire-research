from sqlalchemy import Column, String, Integer,Date
from orml.dbbase import Base
from conf import table_args

class Questionnaire(Base):
    __table_args__ = table_args
    __tablename__ = 'questionnaire'
    questionnaire_id = Column(Integer, primary_key=True)
    questionnaire_user_id = Column(Integer)
    questionnaire_heat = Column(Integer)
    questionnaire_title = Column(String(100))
    questionnaire_intro = Column(String(500))
    questionnaire_classify_id = Column(Integer)
    questionnaire_startdate = Column(Date)
    questionnaire_finishdate = Column(Date)
    questionnaire_complaint_count = Column(Integer)
    questionnaire_total = Column(Integer)
    questionnaire_status = Column(Integer)
    questionnaire_link = Column(String(100))
    questionnaire_flag = Column(Integer)
