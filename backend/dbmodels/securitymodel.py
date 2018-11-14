from sqlalchemy import Column, String, Integer
from orml.dbbase import Base
from conf import table_args

class Security(Base):
    __table_args__ = table_args
    __tablename__ = 'security'
    security_id = Column(Integer, primary_key=True)
    security_user_id = Column(Integer)
    security_question_id = Column(Integer)
    security_answer = Column(String(50))

