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

class Questionnaireorml:
    
    def createquestionnaire(self,usertoken,title,classifyid,finishdate,intro):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,usertoken)
            fdate = datetime.datetime.strptime(finishdate,'%Y-%m-%d')
            ndate = datetime.datetime.now()
            if session.query(User).filter_by(user_id=userid).count()>0 and fdate>ndate:
                session.add(Questionnaire(questionnaire_user_id=userid,questionnaire_title=title,questionnaire_intro
=intro,questionnaire_classify_id=classifyid,questionnaire_startdate=ndate,questionnaire_finishdate
=fdate,questionnaire_status=1,questionnaire_flag=0,questionnaire_complaint_count=0))
                session.commit()
                lastInsertID = session.query(func.max(Questionnaire.questionnaire_id)).one()[0]
                session.close()
                return lastInsertID
            else:
                return False
        except Exception as a:
            print(a)
            return False 
            
    def updatequestionnaire(self,token,questionid,title,finishdate,intro):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                fdate = datetime.datetime.strptime(finishdate,'%Y-%m-%d')
                session.query(Questionnaire).filter_by(questionnaire_id = questionid).update({"questionnaire_title":title,"questionnaire_finishdate":fdate,
                "questionnaire_intro":intro})
                session.commit()
                session.close()
                return True
            else:
                return False
        except Exception as a:
            print(a)
            return False 
            
    def myquestionnaires(self,usertoken,flag):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,usertoken)
            if session.query(User).filter_by(user_id=userid).count()>0:
                questions = session.query(Questionnaire.questionnaire_title,Questionnaire.questionnaire_id).filter_by(questionnaire_user_id=userid,questionnaire_flag=flag).all()
                allValues = []
                for item in questions:
                    value = {}
                    value["subject_title"] = item[0]
                    value["subject_questionnaire_id"] = item[1]
                    allValues.append(value)
                return allValues
            else:
                return "false"
        except Exception as a:
            print(a)
            return False 
            
    def classifycontents(self):
        session = DBSession()
        try:
            if session.query(Classify).count()>0:
                classifies = session.query(Classify.classify_id,Classify.classify_content).all()
                allValues = []
                for item in classifies:
                    value = {}
                    value["classify_id"] = item[0]
                    value["classify_content"] = item[1]
                    allValues.append(value)
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
            if session.query(User).filter_by(user_id=userid).count()>0:
                session.query(Questionnaire).filter_by(questionnaire_id=questionnaireid).delete()
                session.commit()
                session.query(Subject).filter_by(subject_questionnaire_id
=questionnaireid).delete()
                session.commit()
                session.close()
                return True
            else:   
                return False
        except Exception as a:
            print(a)
            return False
            
    def searchquestionnaire(self,key,flag):
        session = DBSession()
        try:
            questions = []
            questions = session.query(Questionnaire.questionnaire_id,Questionnaire.questionnaire_title,
            Questionnaire.questionnaire_startdate,Questionnaire.questionnaire_user_id,
            Questionnaire.questionnaire_finishdate).filter(Questionnaire.questionnaire_title.like('%'+key+'%')).filter_by(questionnaire_flag = flag).all()
            if len(questions)>0:
                allValues = []
                for item in questions:
                    value = {}
                    value["questionnaire_id"] = item[0]
                    value["questionnaire_title"] = item[1]
                    value["questionnaire_startdate"] = str(item[2])
                    username = session.query(User.user_name).filter_by(user_id = item[3]).one()[0]
                    value["questionnaire_username"] = username
                    value["questionnaire_finishdate"] = str(item[4])
                    allValues.append(value)
                return allValues
            else:   
                return 'false'
        except Exception as a:
            print(a)
            return False 
            
    def quicksearch(self,key,flag):
        session = DBSession()
        try:
            questions = []
            questions = session.query(Questionnaire.questionnaire_id,Questionnaire.questionnaire_title).filter(Questionnaire.questionnaire_title.like('%'+key+'%')).filter_by(questionnaire_flag = flag).all()
            if len(questions)>0:
                allValues = []
                for item in questions:
                    value = {}
                    value["questionnaire_id"] = item[0]
                    value["questionnaire_title"] = item[1]
                    allValues.append(value)
                return allValues
            else:    
                return 'false'
        except Exception as a:
            print(a)
            return False 
            
    def allquestionnaires(self):
        session = DBSession()
        try:
            ids = session.query(Questionnaire.questionnaire_id).order_by(desc(Questionnaire.questionnaire_heat)).filter_by(questionnaire_flag=0).all()
            if len(ids)>0:
                allValues = []
                for i in ids:
                    questionnaireid = i[0]
                    value = {}
                    value["questionnaire_id"] = questionnaireid
                    
                    title = session.query(Questionnaire.questionnaire_title).filter_by(questionnaire_id = questionnaireid).one()[0]
                    value["questionnaire_title"] = title
                    
                    userid = session.query(Questionnaire.questionnaire_user_id).filter_by(questionnaire_id = questionnaireid).one()[0]
                    username = session.query(User.user_name).filter_by(user_id = userid).one()[0]
                    value["questionnaire_username"] = username
                    
                    classifyid = session.query(Questionnaire.questionnaire_classify_id).filter_by(questionnaire_id = questionnaireid).one()[0]
                    classifycontent = session.query(Classify.classify_content).filter_by(classify_id = classifyid).one()[0]
                    value["classify_content"] = classifycontent
                    
                    allValues.append(value)
                
                return allValues
            else:
                return False
        except Exception as a:
            print(a)
            return False 
            
    def publishquestionnaire(self,token,questionid):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                session.query(Questionnaire).filter_by(questionnaire_id=questionid).update({"questionnaire_flag":0,"questionnaire_heat":0,"questionnaire_status":1})
                session.commit()
                link = session.query(Questionnaire.questionnaire_link).filter_by(questionnaire_id=questionid).one()[0]
                result = {}
                result["questionnaire_link"] = link
                return result
            else:
                return False
        except Exception as a:
            print(a)
            return False 
            
            
    def getquestionnaireid(self,token):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                
                info = {}
                title = session.query(Questionnaire.questionnaire_title,Questionnaire.questionnaire_intro,
                Questionnaire.questionnaire_id).filter_by(questionnaire_user_id = userid).order_by(desc(Questionnaire.questionnaire_id)).first()
                info["questionnaire_title"] = title[0]
                info["questionnaire_intro"] = title[1]
                info["questionnaire_id"] = title[2]
                return info
            else:
                return False
        except Exception as a:
            print(a)
            return False  
            
    def savetemplate(self,token,questionid):   
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                session.add(Questionnaire(questionnaire_flag=1))
                session.commit()
                lastInsertQuestionID = session.query(func.max(Questionnaire.questionnaire_id)).one()[0]
                print(lastInsertQuestionID)
                result = session.query(Questionnaire.questionnaire_title,Questionnaire.questionnaire_intro,
                Questionnaire.questionnaire_classify_id).filter_by(questionnaire_id = questionid).one()
                ndate = datetime.datetime.now()
                session.query(Questionnaire).filter_by(questionnaire_id = lastInsertQuestionID).update({"questionnaire_user_id":userid,"questionnaire_title":result[0],"questionnaire_intro":result[1],"questionnaire_classify_id":result[2],"questionnaire_startdate":ndate,"questionnaire_flag":1})
                session.commit()
                subject = session.query(Subject.subject_title,Subject.subject_option_flag,Subject.subject_id).filter_by(subject_questionnaire_id = questionid).all()
                for item in subject:
                    session.add(Subject(subject_title = item[0],subject_option_flag = item[1],subject_questionnaire_id = lastInsertQuestionID))
                    session.commit()
                    lastInsertSubjectID = session.query(func.max(Subject.subject_id)).one()[0]
                    optlist = session.query(Optiontable.option_content).filter_by(option_subject_id = item[2]).all()
                    for i in optlist:
                        print(i)
                        session.add(Optiontable(option_subject_id = lastInsertSubjectID,option_content=i[0]))
                        session.commit()
                session.close()
        except Exception as a:
            print(a)
            return False
            
    def questionnairelink(self,token,questionid):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                link = session.query(Questionnaire.questionnaire_link).filter_by(questionnaire_id=questionid).one()[0]
                if link.strip()=='':
                    return False
                else:
                    return link
            else:
                return False
        except Exception as a:
            print(a)
            return False 
            
    def templateshow(self,token,classifyid):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                tmp = session.query(Questionnaire.questionnaire_id,Questionnaire.questionnaire_title).filter_by(questionnaire_user_id = userid,questionnaire_flag=1).all()
                
                allValues = []
                for item in tmp:
                    value = {}
                    number = session.query(Subject.subject_id).filter_by(subject_questionnaire_id=item[0]).count()
                    print('id'+str(item[0]))
                    value["questionnaire_id"] = item[0]
                    value["questionnaire_title"] = item[1]
                    value["subject_number"]=number
                    allValues.append(value)
                return allValues
        except Exception as a:
            print(a)
            return False  
    
    def questionnaireshow(self,token,flag):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                tmp = session.query(Questionnaire.questionnaire_id,Questionnaire.questionnaire_title,Questionnaire.questionnaire_startdate).filter_by(questionnaire_user_id = userid,questionnaire_flag=flag).all()
                allValues = []
                for item in tmp:
                    value = {}
                    number = session.query(Subject).filter_by(subject_questionnaire_id=item[0]).count()
                    value["questionnaire_id"] = item[0]
                    value["questionnaire_title"] = item[1]
                    allValues.append(value)
                return allValues
            else:
                return False
        except Exception as a:
            print(a)
            return False  
            
    def createsubjectitem(self,token,questionid,title,flag,options):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                session.add(Subject(subject_questionnaire_id = questionid,subject_title = title,subject_option_flag = flag))
                session.commit()
                lastInsertSubjectID = session.query(func.max(Subject.subject_id)).one()[0]
                print('*'*10+str(lastInsertSubjectID))
                if flag != 3 and options != '':
                    optlist=demjson.decode(options)
                    for item in optlist:
                        print("*"*10+str(item))    
                        session.add(Optiontable(option_subject_id = lastInsertSubjectID,option_content = item["option_content"],option_total=0))
                        session.commit()
                return lastInsertSubjectID
            else:
                return False
        except Exception as a:
            print(a)
            return False
        
    def getsubjectid(self,token,subjectid):  
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                title = session.query(Subject.subject_title).filter_by(subject_id = subjectid).one()[0]
                flag = session.query(Subject.subject_option_flag).filter_by(subject_id = subjectid).one()[0]
                options = session.query(Optiontable.option_content).filter_by(option_subject_id = subjectid).all()
                content = []
                for item in options:
                    tmp = {}
                    tmp["option_content"] = item[0]
                    print(item[0])
                    content.append(tmp)
                result = {}
                result["subject_title"] = title
                result["subject_option_flag"] = flag
                result["options"] = content
                return result
        except Exception as a:
            print(a)
            return False
            
    def deletesubject(self,token,subjectid): 
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                session.query(Subject).filter_by(subject_id = subjectid).delete()
                session.query(Optiontable).filter_by(option_subject_id = subjectid).delete()
                session.commit()
                session.close()
                return True
        except Exception as a:
            print(a)
            return False
            
    def updatesubject(self,token,subjectid,title,options):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                session.query(Subject).filter_by(subject_id = subjectid).update({"subject_title":title})
                session.query(Optiontable).filter_by(option_subject_id = subjectid).delete()
                optlist=demjson.decode(options)
                for item in optlist:    
                    session.add(Optiontable(option_content = item["option_content"],option_subject_id = subjectid))
                    session.commit()
                session.commit()
                session.close()    
        except Exception as a:
            print(a)
            return False   
            
    def questionnairedetail(self,token,questionid): 
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                tmp = session.query(Questionnaire.questionnaire_title,
                Questionnaire.questionnaire_intro).filter_by(questionnaire_id = questionid).one()
                questionnaire_detail = []
                subjects = session.query(Subject.subject_option_flag,Subject.subject_title,Subject.subject_id).filter_by(subject_questionnaire_id = questionid).all()
                for item in subjects:
                    subject = {}
                    subject["subject_option_flag"] = item[0]
                    subject["subject_title"] = item[1]
                    subject["subject_id"] = item[2]
                    options = []
                    option = session.query(Optiontable.option_content,Optiontable.option_total,Optiontable.option_percent).filter_by(option_subject_id = item[2]).all()
                    for i in option:
                        temp = {}
                        temp["option_content"] = i[0]
                        temp["option_total"] = i[1]
                        temp["option_percent"] = i[2]
                        options.append(temp)
                    subject["subject_options"] = options
                    questionnaire_detail.append(subject)
                allValues = {}
                allValues["questionnaire_title"] = tmp[0]
                allValues["questionnaire_intro"] = tmp[1]
                allValues["questionnaire_detail"] = questionnaire_detail
                return allValues
            else:
                return False
        except Exception as a:
            print(a)
            return False   
            
    def questionnaireclassify(self,token,classify):
        session = DBSession()
        try:
            userid=Userorml.getidbytoken(self,token)
            if session.query(User).filter_by(user_id=userid).count()>0:
                questions = session.query(Questionnaire.questionnaire_id,Questionnaire.questionnaire_title).filter_by(questionnaire_classify_id = classify,questionnaire_flag = 1).all()
                allValues = []
                for item in questions:
                    question = {}
                    count = session.query(Subject).filter_by(subject_questionnaire_id = item[0]).count()
                    question["questionnaire_title"] = item[1]
                    question["questionnaire_id"] = item[0]
                    question["subject_number"] = count
                    allValues.append(question)
                return allValues
            else:
                return False
        except Exception as a:
            print(a)
            return False
            
            
            
