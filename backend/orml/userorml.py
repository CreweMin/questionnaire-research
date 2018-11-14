from orml.dbbase import DBSession
from dbmodels.usermodel import User
from dbmodels.usertokenmodel import Usertoken
from dbmodels.secretmodel import Secret
from dbmodels.securitymodel import Security
from orml.dbbase import engine
from sqlalchemy.sql import func
import uuid

class Userorml:

    def checkuserexist(self, username):
        session = DBSession()
        try:
            if session.query(User).filter_by(user_name=username).count() > 0:
                return True   
        except Exception as a:
            print(a)
            return "False"
        else:
            return False
    
    def getsecretquestions(self):
        session = DBSession()
        try:
            if session.query(Secret).count() > 0:
                questions = []
                allValues = session.query(Secret.secret_question_id,Secret.secret_content).all()
                print(allValues)
                for question in allValues:
                    item = {}
                    item["secret_question_id"] = question[0]
                    item["secret_content"] = question[1]
                    questions.append(item)
                return questions
        except Exception as a:
            print(a)
            return "False"
        else:
            return False
              
            
    def adduser(self, username, password,quetion_id,answer):
        session = DBSession()
        try:
            if username != "" and not self.checkuserexist(username):
                session.add(User(user_name=username,
                                 user_password=password,
                                 user_role_id=1))
                session.commit()
                '''这里需要使用sqlalchmy中的func.max(User.user_id)函数返回插入user后的主键'''
                lastInsertID = session.query(func.max(User.user_id)).one()[0]                            
                session.add(Security(security_user_id
=lastInsertID,security_question_id=quetion_id,security_answer=answer))
                session.commit()
                session.close()
                return True
            else:
                return False
        except Exception as a:
            print(a)
        else:
            return "数据库错误"
            
      
    def checklogin(self, username, password):
        session = DBSession()
        try:
            if session.query(User).filter_by(user_name=username, user_password=password).count() > 0:
                usertoken = str(uuid.uuid4())
                userid = session.query(User.user_id).filter_by(user_name=username, user_password=password)
                session.add(Usertoken(user_id=userid,user_token=usertoken))
                return True
            else:
                return False
        except Exception as a:
            print(a)
            return "数据库错误"
             
    def getidbyname(self,username):
        session = DBSession()
        try:
            if session.query(User).filter_by(user_name=username).count() > 0:
                userid = session.query(User.user_id).filter_by(user_name=username).all()
                userid = userid[0][0]
                session.commit()
                session.close()
            else:
                return "false"
        except Exception as a:
            print(a)
            return False
        else:
            return userid
            
    def usertokenadd(self,username):
        session =DBSession()
        try:
            usertoken = str(uuid.uuid4())
            userid = self.getidbyname(username)
            session.add(Usertoken(user_token=usertoken,user_id=userid))
            session.commit()
            session.close()  
        except Exception as a:
            print(a) 
            return False    
        else:
            return usertoken      
            
    
            
    def tokendelete(self, usertoken):
        session = DBSession()
        try:
            session.query(Usertoken).filter_by(user_token=usertoken).delete()
            session.commit()
            session.close()
        except Exception as a:
            print(a)
            return False
        else:
            return True   
            
    def showquestion(self,username):
        session = DBSession()
        try:
            print(str('*')*50)
            if session.query(User).filter_by(user_name=username).count()==0:
                return "false"
            else:
                userid = session.query(User.user_id).filter_by(user_name=username).one()
            secretid = session.query(Security.security_question_id
).filter_by(security_user_id=userid[0]).one()
            secret = session.query(Secret.secret_content).filter_by(secret_question_id=secretid[0]).one()
            content={}
            content["secret_content"] = secret[0]
            if(secret[0] == ''):
                return "false"
            else:
                return content
        except Exception as a:
            print(a)
            return False 
            
    def checksecurity(self,username,answer):
        session = DBSession()
        try:
            if session.query(User).filter_by(user_name=username).count()==0:
                return False
            else:
                userid = session.query(User.user_id).filter_by(user_name=username).one()
            trueanswer = session.query(Security.security_answer
).filter_by(security_user_id=userid[0]).one()
            if(trueanswer[0] == answer):
                return True
            else:
                return "false"
        except Exception as a:
            print(a)
            return False 
            
    def findpassword(self,username,password):
        session = DBSession()
        try:
            if session.query(User).filter_by(user_name=username).count()==0:
                return False
            else:
                userid = session.query(User).filter_by(user_name=username).update({'user_password':password})
                session.commit()
                session.close()
                return True
        except Exception as a:
            print(a)
            return False 
            
    def checkoldpassword(self,usertoken,oldpassword):
        session = DBSession()
        try:
            if session.query(Usertoken).filter_by(user_token=usertoken).count()==0:
                return False
            else:
                userid = self.getidbytoken(usertoken)
                if session.query(User).filter_by(user_password = oldpassword).count()>0:
                    return True
                else:
                    return "false"
        except Exception as a:
            print(a)
            return False 
            
    def modifypassword(self,usertoken,oldpassword,newpassword):
        session = DBSession()
        try:
            userid = self.getidbytoken(usertoken)
            if session.query(User).filter_by(user_id=userid,user_password=oldpassword).count()>0:
                session.query(User).filter_by(user_id=userid,user_password=oldpassword).update({"user_password":newpassword})
                session.commit()
                session.close()
                return True
            else:
                return False
        except Exception as a:
            print(a)
            return False 
            
    def showusername(self,usertoken):
        session = DBSession()
        try:
            userid = self.getidbytoken(usertoken)
            userrole = session.query(User.user_role_id).filter_by(user_id=userid).one()[0]
            user_name = {}
            if userrole == 1:
                name = session.query(User.user_name).filter_by(user_id=userid).one()[0]
                user_name["user_name"] = name
                user_name["role_id"] = 1
                return user_name
            elif userrole == 2:
                user_name["user_name"] = "超级管理员"
                user_name["role_id"] = 2
                return user_name
            else:
                return False
        except Exception as a:
            print(a)
            return False 
            
    def getnamebytoken(self, usertoken):
        session = DBSession()
        try:
            userid = session.query(Usertoken.user_id).filter_by(user_token=usertoken).all()
            userid = userid[0][0]
            username = session.query(User.user_name).filter_by(user_id=userid).all()
            username = username[0][0]
            session.commit()
            session.close()  
        except Exception as a:
            print(a)
            return False
        else:
            return username
            
    def getidbytoken(self, usertoken):
        session = DBSession()
        try:
            userid = session.query(Usertoken.user_id).filter_by(user_token=usertoken).all()
            userid = userid[0][0]
            session.commit()
            session.close()  
        except Exception as a:
            print(a)
            return False
        else:
            return userid


            
