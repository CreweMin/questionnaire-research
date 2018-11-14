from orml.dbbase import DBSession
from dbmodels.usermodel import User
from dbmodels.securitymodel import Security
from dbmodels.secretmodel import Secret
from dbmodels.rolemodel import Role
from dbmodels.questionnairemodel import Questionnaire
from dbmodels.classifymodel import Classify 
from dbmodels.subjectmodel import Subject
from dbmodels.optiontablemodel import Optiontable
from dbmodels.interlocutionmodel import Interlocution
from dbmodels.usertokenmodel import Usertoken
from dbmodels.searchlogmodel import Searchlog

session = DBSession()

if session.query(Secret).count() == 0:
    secretlist = [Secret(secret_content = "你的学号是多少？"),Secret(secret_content = "你的生日是哪天？")]
    for i in secretlist:
        session.add(i)
        
if session.query(Classify).count() == 0:
    classifylist = [Classify(classify_content = "学术教育"),Classify(classify_content = "社会民意"),Classify(classify_content = "医疗")]
    for i in classifylist:
        session.add(i)
        
if session.query(Role).count() == 0:
    rolelist = [Role(role_content = "普通用户"),Role(role_content = "超级管理员")]
    for i in rolelist:
        session.add(i)
        
if session.query(User).count() == 0:
    userlist = [User(user_id=3,user_name = 'long',user_password = 'long',user_role_id = 1),Usertoken(user_id = 3,user_token = 'd17882c9-dd71-4b13-8e49-e7f0e62e905a'),User(user_id=1,user_name = 'jack',user_password = '123456',user_role_id = 2),Usertoken(user_id = 1,user_token = 'a17882c9-dd71-4b13-8e49-e7f0e62e905b')]
    for i in userlist:
        session.add(i)
        
session.commit()
session.close()
