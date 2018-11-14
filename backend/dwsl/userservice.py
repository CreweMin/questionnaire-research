from flask.ext import restful
from flask import request
from flask import jsonify
from flask import Response
from tools.info import Info
from conf import httpserver, httpport
from tools.crossdomain import allow_cross_domain
from orml.userorml import Userorml


class CheckUserExist(restful.Resource):

    @allow_cross_domain
    def get(self):
        username = request.args.get("user_name")
        uo = Userorml()
        name = uo.checkuserexist(username)
        if name == "False":
            return jsonify(Info(False,'数据库错误',None).tojson())
        elif not name:
            return jsonify(Info(True,'可用的用户名',None).tojson())
        else:
            return jsonify(Info(False,'用户名已存在',None).tojson())
        
class GetSecretQuestions(restful.Resource):

    @allow_cross_domain
    def get(self):
        uo = Userorml()
        questions = uo.getsecretquestions()
        if questions == "False":
            return jsonify(Info(False,'数据库错误',None).tojson())
        else:
            return jsonify(Info(True,'返回成功',questions).tojson())
       
class AddUser(restful.Resource):

    @allow_cross_domain
    def post(self):
        username = request.form["user_name"]
        password = request.form["user_password"]
        quetion_id = request.form["security_question_id"]
        answer = request.form["security_answer"]
        print("@@@@")
        uo = Userorml()
        if uo.adduser(username, password,quetion_id,answer):
            return jsonify(Info(True, '注册成功').tojson())
        else:
            return jsonify(Info(False, '数据库错误').tojson())
       
class CheckLogin(restful.Resource):

    @allow_cross_domain
    def post(self):
        username = request.form["user_name"]
        password = request.form["user_password"]
        uo = Userorml()
        temp = uo.checklogin(username,password)
        usertoken = uo.usertokenadd(username)
        if temp == "数据库错误":
            return jsonify(Info(False, '数据库错误').tojson())
        elif temp:
            return jsonify(Info(True, '登录成功',usertoken).tojson())
        else:
            return jsonify(Info(False, '用户名或密码错误').tojson())
            
class TokenDelete(restful.Resource):
    
    @allow_cross_domain
    def get(self):
        usertoken = request.args.get("usertoken")
        uo = Userorml()
        if not uo.tokendelete(usertoken) :
            return jsonify(Info(False, "数据库错误").tojson())
        else:
            return jsonify(Info(True, " 成功删除usertoken").tojson())

class ShowQuestion(restful.Resource):

    @allow_cross_domain
    def get(self):
        username = request.args.get("user_name")
        uo = Userorml()
        content = uo.showquestion(username)
        if content == "false":
            return jsonify(Info(False, "数据库不存在此用户").tojson())
        elif content == False :
            return jsonify(Info(False, "数据库错误").tojson())
        else:
            return jsonify(Info(True, "返回成功",content).tojson())
            
class CheckSecurity(restful.Resource):

    @allow_cross_domain
    def get(self):
        username = request.args.get("user_name")
        answer = request.args.get("security_answer")
        print(answer)
        content = request.args.get("secret_content")
        uo = Userorml()
        flag = uo.checksecurity(username,answer)
        if flag == "false":
            return jsonify(Info(False, "密保问题或者答案输入错误").tojson())
        elif flag == False:
            return jsonify(Info(False, "数据库错误").tojson())
        else:
            return jsonify(Info(True, "密保答案输入正确").tojson())
            
class FindPassword(restful.Resource):

    @allow_cross_domain
    def post(self):
        username = request.form["user_name"]
        password = request.form["user_password"]
        uo = Userorml()
        flag = uo.findpassword(username,password)
        if flag == False:
            return jsonify(Info(False, "数据库错误").tojson())
        else:
            return jsonify(Info(True, "成功找回密码").tojson())
            
class CheckOldpassword(restful.Resource):

    @allow_cross_domain
    def get(self):
        usertoken = request.args.get("usertoken")
        oldpassword = request.args.get("user_oldpassword")
        uo = Userorml()
        flag = uo.checkoldpassword(usertoken,oldpassword)
        if flag == "false":
            return jsonify(Info(False, "原密码输入错误").tojson())
        elif flag == False:
            return jsonify(Info(False, "数据库错误").tojson())
        else:
            return jsonify(Info(True, "原密码输入正确").tojson())
            
class ModifyPassword(restful.Resource):

    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken"]
        oldpassword = request.form["user_oldpassword"]
        newpassword = request.form["user_newpassword"]
        uo = Userorml()
        flag = uo.modifypassword(usertoken,oldpassword,newpassword)
        if flag == False:
            return jsonify(Info(False, "数据库错误").tojson())
        else:
            return jsonify(Info(True, "密码修改成功").tojson())
            
class ShowUserName(restful.Resource):

    @allow_cross_domain
    def get(self):
        usertoken = request.args.get("usertoken")
        uo = Userorml()
        username = uo.showusername(usertoken)
        if username == False:
            return jsonify(Info(False, "数据库错误").tojson())
        else:
            return jsonify(Info(True, "返回成功",username).tojson())
        

class Getidbyname(restful.Resource):

    @allow_cross_domain
    def get(self):
        username = request.args.get("user_name")
        uo = Userorml()
        userid = uo.getidbyname(username)
        if userid =="false":
            return jsonify(Info(False, "不存在的用户名！").tojson())
        elif not userid :
            return jsonify(Info(False, "数据库错误！").tojson())
        else:
            return jsonify(Info(True, "用户名查询成功！",userid).tojson())

            
            
class Getnamebytoken(restful.Resource):
    
    @allow_cross_domain
    def get(self):
        usertoken = request.args.get("usertoken")
        uo = Userorml()
        username = uo.getnamebytoken(usertoken)
        if username:
            return jsonify(Info(True, "查询用户名成功",username).tojson())
        else:
            return jsonify(Info(False, "数据库错误").tojson())
            
class Getidbytoken(restful.Resource):
    
    @allow_cross_domain
    def get(self):
        usertoken = request.args.get("usertoken")
        uo = Userorml()
        userid = uo.getidbytoken(usertoken)
        if userid:
            return jsonify(Info(True, "查询用户编号成功",userid).tojson())
        else:
            return jsonify(Info(False, "数据库错误").tojson())


