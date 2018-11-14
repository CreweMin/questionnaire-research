#! /usr/bin/env python
#coding=utf-8
from flask.ext import restful
from flask import request
from flask import jsonify
from flask import Response
from tools.info import Info
from conf import httpserver, httpport
from tools.crossdomain import allow_cross_domain
from orml.questionnaireorml import Questionnaireorml

class CreateQuestionnaire(restful.Resource):

    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken"]
        title = request.form["questionnaire_title"]
        classifyid = request.form["classify_id"]
        intro = request.form["questionnaire_intro"]
        finishdate = request.form["questionnaire_finishdate"]
        qo = Questionnaireorml()
        questionnaireid = qo.createquestionnaire(usertoken,title,classifyid,finishdate,intro)
        if questionnaireid == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '成功创建问卷',questionnaireid).tojson())
            
class UpdateQuestionnaire(restful.Resource):

    @allow_cross_domain
    def post(self):
        token = request.form["usertoken"]
        questionid = request.form["questionnaire_id"]
        title = request.form["questionnaire_title"]
        intro = request.form["questionnaire_intro"]
        finishdate = request.form["questionnaire_finishdate"]
        qo = Questionnaireorml()
        result = qo.updatequestionnaire(token,questionid,title,finishdate,intro)
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '成功修改问卷').tojson())
        
            
class QuestionnaireShow(restful.Resource):

    @allow_cross_domain
    def get(self):
        usertoken = request.args.get("usertoken")
        flag = request.args.get("questionnaire_flag")
        print('*'*20)
        qo = Questionnaireorml()
        allValues = qo.myquestionnaires(usertoken,flag)
        if allValues == "false":
            return jsonify(Info(False, '您还未创建问卷').tojson())
        elif allValues == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(False, '返回成功',allValues).tojson())
            
class ClassifyContents(restful.Resource):

    @allow_cross_domain
    def get(self):
        qo = Questionnaireorml()
        allValues = qo.classifycontents()
        if allValues == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(False, '返回成功',allValues).tojson())
            
class DeleteQuestionnaire(restful.Resource):

    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken"]
        questionnaireid = request.form["questionnaire_id"]
        qo = Questionnaireorml()
        flag = qo.deletequestionnaire(usertoken,questionnaireid)
        if flag == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '问卷删除成功').tojson())
            
class SearchQuestionnaire(restful.Resource):

    @allow_cross_domain
    def get(self):
        key = request.args.get("key_words")
        flag = request.args.get("questionnaire_flag")
        qo = Questionnaireorml()
        questions = qo.searchquestionnaire(key,flag)
        if questions == False:
            return jsonify(Info(False, '数据库错误').tojson())
        elif questions == 'false':
            return jsonify(Info(False, '没有相关数据').tojson())
        else:
            return jsonify(Info(True, '搜索结果',questions).tojson())

class QuickSearch(restful.Resource):

    @allow_cross_domain
    def get(self):
        key = request.args.get("key_words")
        flag = request.args.get("questionnaire_flag")
        qo = Questionnaireorml()
        result = qo.quicksearch(key,flag)
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        elif result == 'false':
            return jsonify(Info(False, '没有相关数据').tojson())
        else:
            return jsonify(Info(True, '搜索结果',result).tojson())
            
class AllQuestionnaires(restful.Resource):

    @allow_cross_domain
    def get(self):
        qo = Questionnaireorml()
        result = qo.allquestionnaires()
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '返回条数',result).tojson())
            
class PublishQuestionnaire(restful.Resource):

    @allow_cross_domain
    def post(self):
        token = request.form["usertoken"]
        questionid = request.form["questionnaire_id"]
        qo = Questionnaireorml()
        flag = qo.publishquestionnaire(token,questionid)
        if flag == False:
            return jsonify(Info(False, '数据库错误').tojson())
        elif flag == 'false':
            return jsonify(Info(False, '题目不能为空').tojson())
        else:
            return jsonify(Info(True, '成功发布问卷',flag).tojson())
            
#class GetQuestionnaireId(restful.Resource):

#    @allow_cross_domain
#    def get(self):
#        questionid = request.args.get("questionnaire_id")
#        qo = Questionnaireorml()
#        info = qo.getquestionnaireid(questionid)
#        if info == False:
#            return jsonify(Info(False, '数据库错误').tojson())
#        else:
#            return jsonify(Info(True, '返回成功',info).tojson())
#            
class GetQuestionnaireId(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        qo = Questionnaireorml()
        info = qo.getquestionnaireid(token)
        if info == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '返回成功',info).tojson())
            
class SaveTemplate(restful.Resource):

    @allow_cross_domain
    def post(self):
        token = request.form["usertoken"]
        questionid = request.form["questionnaire_id"]
        qo = Questionnaireorml()
        flag = qo.savetemplate(token,questionid)
        if flag == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '成功保存模板').tojson())
            
class QuestionnaireLink(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        questionid = request.args.get("questionnaire_id")
        qo = Questionnaireorml()
        link = qo.questionnairelink(token,questionid)
        if link == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '返回成功',link).tojson())
            
class TemplateShow(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        classifyid = request.args.get("classfy_id")
        qo = Questionnaireorml()
        result = qo.templateshow(token,classifyid)
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, {"template_number":len(result)},result).tojson())
            
class QuestionnaireShow(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        flag = request.args.get("questionnaire_flag")
        qo = Questionnaireorml()
        result = qo.questionnaireshow(token,flag)
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, {"template_number":len(result)},result).tojson())
            
class CreateSubjectItem(restful.Resource):

    @allow_cross_domain
    def post(self):
        token = request.form["usertoken"]
        questionid = request.form["questionnaire_id"]
        title = request.form["subject_title"]
        flag = request.form["subject_option_flag"]
        print(flag)
        options = request.form["options"]
        print(options)
        qo = Questionnaireorml()
        result = qo.createsubjectitem(token,questionid,title,flag,options)
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True,'返回成功',{"subject_id":result}).tojson())
            
class GetSubjectId(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        subjectid = request.args.get("subject_id")
        qo = Questionnaireorml()
        result = qo.getsubjectid(token,subjectid)
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True,'返回成功',result).tojson())
            
class DeleteSubject(restful.Resource):

    @allow_cross_domain
    def post(self):
        token = request.form["usertoken"]
        subjectid = request.form["subject_id"]
        qo = Questionnaireorml()
        result = qo.deletesubject(token,subjectid)
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True,'成功删除').tojson())
            
class UpdateSubject(restful.Resource):

    @allow_cross_domain
    def post(self):
        token = request.form["usertoken"]
        subjectid = request.form["subject_id"]
        title = request.form["subject_title"]
        options = request.form["options"]
        qo = Questionnaireorml()
        result = qo.updatesubject(token,subjectid,title,options)
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True,'成功修改').tojson())
            
class QuestionnaireDetail(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        questionid = request.args.get("questionnaire_id")
        qo = Questionnaireorml()
        result = qo.questionnairedetail(token,questionid)
        if result == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True,'返回成功',result).tojson())      
            
class QuestionnaireClassify(restful.Resource):

    @allow_cross_domain
    def get(self):
        token = request.args.get("usertoken")
        classify = request.args.get("classify_id")
        qo = Questionnaireorml()
        allValues = qo.questionnaireclassify(token,classify)
        if allValues == False:
            return jsonify(Info(False, '数据库错误').tojson())
        else:
            return jsonify(Info(True, '成功返回',allValues).tojson())  
       
       
       
       
        
