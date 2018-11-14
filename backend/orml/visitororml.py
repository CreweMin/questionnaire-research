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
import time,datetime
import uuid
import demjson
class Visitororml:

    def openlink(self,link):
        session = DBSession()
        try:
            session.query(Questionnaire).filter_by(questionnaire_id = questionid).update({"questionnaire_heat":Questionnaire.questionnaire_heat+1})
            session.commit()
            tmp = session.query(Questionnaire.questionnaire_title,Questionnaire.questionnaire_intro,
            Questionnaire.questionnaire_id).filter_by(questionnaire_link = link).one()
            questionid = tmp[2]
            questionnaire_detail = []
            subjects = session.query(Subject.subject_option_flag,Subject.subject_title,Subject.subject_id).filter_by(subject_questionnaire_id = questionid).all()
            for item in subjects:
                subject = {}
                subject["subject_option_flag"] = item[0]
                subject["subject_title"] = item[1]
                options = []
                option = session.query(Optiontable.option_content,Optiontable.option_id).filter_by(option_subject_id = item[2]).all()
                for i in option:
                    temp = {}
                    temp["option_content"] = i[0]
                    temp["option_id"] = i[1]
                    options.append(temp)
                subject["subject_options"] = options
                questionnaire_detail.append(subject)
            allValues = {}
            allValues["questionnaire_title"] = tmp[0]
            allValues["questionnaire_intro"] = tmp[1]
            allValues["questionnaire_detail"] = questionnaire_detail
            return allValues
        except Exception as a:
            print(a)
            return False
            
    def fillin(self,questionid,options): 
        session = DBSession()
        try:
            ndate = datetime.date.today()
            fdate = session.query(Questionnaire.questionnaire_finishdate).filter_by(questionnaire_id = questionid).one()[0]
            if ndate > fdate:
                return 'false'
            else:
                if options != '':
                    tmp = demjson.decode(options)
                    for item in tmp:
                        flag = session.query(Subject.subject_option_flag).filter_by(subject_id = item["subject_id"]).one()[0]
                        if flag == 3:
                            session.add(Interlocution(interlocution_content
=item["interlocution_content"],interlocution_subject_id = item["subject_id"]))
                            session.commit()
                        else:
                            session.query(Optiontable).filter_by(option_subject_id = item["subject_id"],option_id = item["option_id"]).update({"option_total":Optiontable.option_total+1})
                            session.commit()
                            count = session.query(Optiontable.option_total).filter_by(option_subject_id = item["subject_id"],option_id = item["option_id"]).one()[0]
                            allvalues = session.query(Optiontable.option_total).filter_by(option_subject_id = item["subject_id"]).all()
                            su = 0
                            for i in allvalues:
                                su = su + i[0]
                            percent = count / su
                            session.query(Optiontable).filter_by(option_subject_id = item["subject_id"],option_id = item["option_id"]).update({"option_percent":percent})
                            session.commit()
                        
        except Exception as a:
            print(a)
            return False
            
    def alarm(self,questionid):
        session = DBSession()
        try:
            session.query(Questionnaire).filter_by(questionnaire_id = questionid).update({"questionnaire_complaint_count":Questionnaire.questionnaire_complaint_count
+1})
            session.commit()
            session.close()
        except Exception as a:
            print(a)
            return False
            
            
            
    def opentitle(self,link):
        session = DBSession()
        try:
            session.query(Questionnaire).filter_by(questionnaire_id = link).update({"questionnaire_heat":Questionnaire.questionnaire_heat+1})
            session.commit()
            tmp = session.query(Questionnaire.questionnaire_title,Questionnaire.questionnaire_intro,
            Questionnaire.questionnaire_id).filter_by(questionnaire_id = link).one()
            questionid = tmp[2]
            questionnaire_detail = []
            subjects = session.query(Subject.subject_option_flag,Subject.subject_title,Subject.subject_id).filter_by(subject_questionnaire_id = questionid).all()
            for item in subjects:
                subject = {}
                subject["subject_option_flag"] = item[0]
                subject["subject_title"] = item[1]
                subject["subject_id"] = item[2]
                options = []
                option = session.query(Optiontable.option_content,Optiontable.option_id).filter_by(option_subject_id = item[2]).all()
                for i in option:
                    temp = {}
                    temp["option_content"] = i[0]
                    temp["option_id"] = i[1]
                    options.append(temp)
                subject["subject_options"] = options
                questionnaire_detail.append(subject)
            allValues = {}
            allValues["questionnaire_title"] = tmp[0]
            allValues["questionnaire_intro"] = tmp[1]
            allValues["questionnaire_detail"] = questionnaire_detail
            return allValues
        except Exception as a:
            print(a)
            return False
            
            
            
            
            
            
            
            
            
            
            
            
