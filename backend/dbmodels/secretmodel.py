from sqlalchemy import Column, String, Integer
from orml.dbbase import Base
from conf import table_args

class Secret(Base):
    __table_args__ = table_args
    __tablename__ = 'secret'
    secret_question_id = Column(Integer, primary_key=True)
    secret_content = Column(String(50))
