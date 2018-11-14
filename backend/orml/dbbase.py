from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:root@0.0.0.0/Questionnaire?use_unicode=0&charset=utf8', echo=True)
DBSession = sessionmaker(bind=engine)
