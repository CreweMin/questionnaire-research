from flask.ext import restful
from flask import request
from flask import jsonify
from flask import Response
from tools.info import Info
from conf import httpserver, httpport
from tools.crossdomain import allow_cross_domain
from orml.visitororml import Visitororml

class OpenLink(restful.Resource):

    @allow_cross_domain
    def get(self):
        link = request.args.get("questionnaire_link")
        vo = Visitororml()
        result = vo.openlink(link)
        if result == False:
            return jsonify(Info(False,'数据库错误',None).tojson())
        else:
            return jsonify(Info(True,'返回成功',result).tojson())
            
class FillIn(restful.Resource):

    @allow_cross_domain
    def post(self):
        questionid = request.form["questionnaire_id"]
        options = request.form["options"]
        vo = Visitororml()
        result = vo.fillin(questionid,options)
        if result == False:
            return jsonify(Info(False,'数据库错误',None).tojson())
        elif result == 'false':
            return jsonify(Info(False,'该问卷已过期',None).tojson())
        else:
            return jsonify(Info(True,'成功填写',None).tojson())
            
class Alarm(restful.Resource):

    @allow_cross_domain
    def post(self):
        questionid = request.form["questionnaire_id"]
        vo = Visitororml()
        result = vo.alarm(questionid)
        if result == False:
            return jsonify(Info(False,'数据库错误',None).tojson())
        else:
            return jsonify(Info(True,'成功举报',None).tojson())
            
class OpenTitle(restful.Resource):

    @allow_cross_domain
    def get(self):
        link = request.args.get("questionnaire_id")
        vo = Visitororml()
        result = vo.opentitle(link)
        if result == False:
            return jsonify(Info(False,'数据库错误').tojson())
        else:
            return jsonify(Info(True,'返回成功',result).tojson())
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
