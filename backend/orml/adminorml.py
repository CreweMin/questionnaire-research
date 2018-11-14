from orml.dbbase import DBSession
from dbmodels.usermodel import User
from dbmodels.usertokenmodel import Usertoken
from dbmodels.secretmodel import Secret
from dbmodels.securitymodel import Security
from dbmodels.questionnairemodel import Questionnaire
from dbmodels.classifymodel import Classify
from dbmodels.interlocutionmodel import Interlocution
from dbmodels.optiontablemodel import Optiontable
from dbmodels.subjectmodel import Subject
from orml.userorml import Userorml
from orml.dbbase import engine
from sqlalchemy.sql import func
from sqlalchemy import desc
import time,datetime
import uuid
import demjson

class Adminorml:

    def allquestionnaires(self,token,flag):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,usertoken)
            if session.query(User).filter_by(user_id=userid,user_role_id = 2).count()>0:
                questions = session.query(Questionnaire.questionnaire_id,Questionnaire.questionnaire_title).filter_by(questionnaire_flag = flag).all()
                allValues = []
                for item in questions:
                    question = {}
                    tmp = session.query(Questionnaire.questionnaire_user_id,Questionnaire.questionnaire_classify_id).filter_by(questionnaire_id = item[0]).one()
                    question["questionnaire_id"] = item[0]
                    question["questionnaire_title"] = item[1]
                    name = session.query(User.user_name).filter_by(user_id = tmp[0]).one()[0]
                    question["user_name"] = name
                    content = session.query(Classify.classify_content).filter_by(classify_id = tmp[1]).one()[0]
                    question["classify_content"] = content
                    allValues.append(question)
                return allValues
            else:
                return False
        except Exception as a:
            print(a)
            return False 
            
    def deletequestionnaire(self,usertoken,questionnaireid):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,usertoken)
            if session.query(User).filter_by(user_id=userid,user_role_id = 2).count()>0:
                session.query(Questionnaire).filter_by(questionnaire_id=questionnaireid).delete()
                session.commit()
                subjectid = session.query(Subject.subject_id).filter_by(subject_questionnaire_id
=questionnaireid).one()[0]
                session.query(Subject).filter_by(subject_questionnaire_id
=questionnaireid).delete()
                session.commit()
                session.query(Optiontable).filter_by(option_subject_id = subjectid).delete()
                session.commit()
                session.close()
                return True
            else:   
                return False
        except Exception as a:
            print(a)
            return False
            

            
    def deleteuser(self,token,userid):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid,user_role_id = 2).count()>0:
                session.query(User).filter_by(user_id = userid).delete()
                session.query(Usertoken).filter_by(user_id = userid).delete()
                session.commit()
                session.close()
                return True
            else:
                return False
        except Exception as a:
            print(a)
            return False
    
    def allusers(self,token):  
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid,user_role_id = 2).count()>0: 
                names = session.query(User.user_name,User.user_id).filter_by(user_role_id = 1).all()
                users = []
                for i in names:
                    user = {}
                    title = session.query(Questionnaire.questionnaire_title).filter_by(questionnaire_user_id = i[1]).order_by(desc(Questionnaire.questionnaire_id)).first()
                    user["user_name"] = i[0]
                    user["user_id"] = i[1]
                    user["questionnaire_title"] = title
                    users.append(user)
                return users
            else:
                return False    
        except Exception as a:
            print(a)
            return False    
            
            
            
            
            
            
            
            
            
            
            
            
