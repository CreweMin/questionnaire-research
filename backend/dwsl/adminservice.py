#! /usr/bin/env python
#coding=utf-8
from flask.ext import restful
from flask import request
from flask import jsonify
from flask import Response
from tools.info import Info
from conf import httpserver, httpport
from tools.crossdomain import allow_cross_domain
from orml.adminorml import Adminorml

class AllQuestionnaire(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        flag = request.args.get("questionnaire_flag")
        ao = Adminorml()
        allValues = ao.allquestionnaires(token,flag)
        if allValues == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '返回成功',allValues).tojson())
            
class QuestionnaireDelete(restful.Resource):

    @allow_cross_domain
    def post(self):
        token = request.form["usertoken"]
        questionid = request.form["questionnaire_id"]
        ao = Adminorml()
        flag = ao.deletequestionnaire(token,questionid)
        if flag == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '成功删除').tojson())
            
class QuestionnaireClassify(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        classify = request.args.get("classify_id")
        ao = Adminorml()
        allValues = ao.questionnaireclassify(token,classify)
        if allValues == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '成功返回',allValues).tojson())
            
class DeleteUser(restful.Resource):

    @allow_cross_domain
    def post(self):
        token = request.form["usertoken"]
        userid = request.form["user_id"]
        ao = Adminorml()
        flag = ao.deleteuser(token,userid)
        if flag == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '成功删除').tojson())
            
class AllUsers(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        ao = Adminorml()
        allValues = ao.allusers(token)
        if allValues == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '成功返回',allValues).tojson())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

