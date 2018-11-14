#! /usr/bin/env python
#coding=utf-8
import urllib
import unittest
import json
import http.client as httplib
import urllib.parse as urllib
from conf import httpserver
from conf import httpport

conn = httplib.HTTPConnection(httpserver, httpport)
header = {"Content-type": "application/x-www-form-urlencoded"}

class TestQuestionnaire(unittest.TestCase):

#    def test_createquestionnaire01(self):
#        global conn
#        global header
#        params = {"usertoken": "d17882c9-dd71-4b13-8e49-e7f0e62e905a",
#                  "questionnaire_title": "高中生信用状况调查",
#                  "classify_id":1,
#                  "questionnaire_finishdate":"2018-07-20",
#                  "questionnaire_intro":"这是针对高中生信用状况的调查"}
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/create/questionnaire/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_createquestionnaire02(self):
#        global conn
#        global header
#        params = {"usertoken": "d17882c9-dd71-4b13-8e49-e7f0e62e905a",
#                  "questionnaire_title": "大学生消费情况调查",
#                  "classify_id":1,
#                  "questionnaire_finishdate":"2017-07-20",
#                  "questionnaire_intro":"这是针对大学生消费状况的调查"}
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/create/questionnaire/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_updatequestionnaire01(self):
#        global conn
#        global header
#        params = {"usertoken": "d17882c9-dd71-4b13-8e49-e7f0e62e905a",
#                  "questionnaire_id":31,
#                  "questionnaire_title": "消费情况调查test",
#                  "questionnaire_finishdate":"2018-07-20",
#                  "questionnaire_intro":"这是消费状况的调查"
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/update/questionnaire/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_myquestionnaires01(self): 
#        global conn
#        global header
#        conn.request('GET', '/v1/questionnaire/show/?usertoken=d17882c9-dd71-4b13-8e49-e7f0e62e905a&questionnaire_flag=0')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_classifycontents(self): 
#        global conn
#        global header
#        conn.request('GET', '/v1/questionnaire/classify/contents/')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_deletequestionnaire01(self):
#        global conn
#        global header
#        params = {"usertoken": "d17882c9-dd71-4b13-8e49-e7f0e62e905a",
#                  "questionnaire_id":2,
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/questionnaire/deletequestionnaire/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_search01(self): 
#        global conn
#        global header
#        url = '/v1/search/questionnaire/?key_words='
#        key_words = "大学生"
#        key = key_words.encode(encoding="utf-8")
#        print(type(key))
#        url = url+str(key)
#        print(url)
#        conn.request('GET', url)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
        
#    def test_search02(self): 
#        global conn
#        global header
#        url = '/v1/search/questionnaire/?key_words='
#        key_words = "医生"
#        key = key_words.encode(encoding="utf-8")
#        url = url+str(key)
#        conn.request('GET', url)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_quicksearch01(self): 
#        global conn
#        global header
#        url = '/v1/quick/search/questionnaire/?key_words='
#        key_words = "大学生"
#        key = key_words.encode(encoding="utf-8")
#        print(type(key))
#        url = url+str(key)
#        print(url)
#        conn.request('GET', url)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_quicksearch02(self): 
#        global conn
#        global header
#        url = '/v1/quick/search/questionnaire/?key_words='
#        key_words = "医生"
#        key = key_words.encode(encoding="utf-8")
#        print(type(key))
#        url = url+str(key)
#        print(url)
#        conn.request('GET', url)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_allquestionnaire(self): 
#        global conn
#        global header
#        url = '/v1/all/questionnaires/'
#        conn.request('GET', url)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])


#    def test_publicquestionnaire01(self):
#        global conn
#        global header
#        params = {"usertoken": "d17882c9-dd71-4b13-8e49-e7f0e62e905a",
#                  "questionnaire_id":1
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/questionnaire/publish/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_publicquestionnaire02(self):
#        global conn
#        global header
#        params = {"usertoken": "d17882c9-dd71-4b13-8e49-e7f0e62e905a",
#                  "questionnaire_detail":[]
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/questionnaire/publish/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_getquestionnaireid(self): 
#        global conn
#        global header
#        conn.request('GET', '/v1/questionnaire/getid/?usertoken=10072a74-811c-473d-b441-baedf4d0b4dc')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

    def test_savetemplate(self):
        global conn
        global header
        params = {"usertoken": "d7ed738c-35e4-4a82-ac4d-dfc8505a5c72",
                  "questionnaire_id":51,
                  }
        params = urllib.urlencode(params)
        conn.request('POST', '/v1/questionnaire/save/template/', params, header)
        data = json.loads(conn.getresponse().read().decode("utf-8"))
        print(data)
        self.assertTrue(data["infostatus"])

#    def test_savetemplate2(self):
#        global conn
#        global header
#        params = {"usertoken": "d17882c9-dd71-4b13-8e49-e7f0e62e905a",
#                  "questionnaire_id":2
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/questionnaire/save/template/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_questionnairelink(self): 
#        global conn
#        global header
#        conn.request('GET', '/v1/questionnaire/link/?questionnaire_id=1&usertoken=d17882c9-dd71-4b13-8e49-e7f0e62e905a')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_templateshow(self): 
#        global conn
#        global header
#        conn.request('GET', '/v1/questionnaire/template/show/?usertoken=d17882c9-dd71-4b13-8e49-e7f0e62e905a&classfy_id=1')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_questionnaireshow(self): 
#        global conn
#        global header
#        conn.request('GET', '/v1/questionnaire/show/?usertoken=d17882c9-dd71-4b13-8e49-e7f0e62e905a&questionnaire_flag=1')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_createsubjectitem01(self):
#        global conn
#        global header
#        params = {"usertoken":'d7ed738c-35e4-4a82-ac4d-dfc8505a5c72',
#                  "questionnaire_id":49,
#                  "subject_option_flag":1,
#                  "subject_title":"您的性别?",
#                  "options":[{"option_content":"男"},{"option_content":"女"}]
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/subject/createitem/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
        
#    def test_createsubjectitem02(self):
#        global conn
#        global header
#        params = {"usertoken":'d17882c9-dd71-4b13-8e49-e7f0e62e905a',
#                  "questionnaire_id":1,
#                  "subject_option_flag":3,
#                  "subject_title":"您对学生如何省钱有什么建议吗?",
#                  "options":''
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/subject/createitem/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_getsubjectid(self): 
#        global conn
#        global header
#        conn.request('GET', '/v1/subject/getid/?subject_id=49&usertoken=d7ed738c-35e4-4a82-ac4d-dfc8505a5c72')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#        
#    def test_deletesubject(self):
#        global conn
#        global header
#        params = {"usertoken":'d17882c9-dd71-4b13-8e49-e7f0e62e905a',
#                  "subject_id":23
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/subject/delete/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_updatesubject01(self):
#        global conn
#        global header
#        params = {"usertoken":'d17882c9-dd71-4b13-8e49-e7f0e62e905a',
#                  "subject_id":7,
#                  "subject_title":"您每月花多少钱",
#                  "options":[{"option_content":"500以下"},{"option_content":"500-1000"},{"option_content":"1000-2000"},{"option_content":"2000以上"}]
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/subject/update/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_questionnairedetail(self): 
#        global conn
#        global header
#        conn.request('GET', '/v1/questionnaire/detail/?usertoken=d7ed738c-35e4-4a82-ac4d-dfc8505a5c72&questionnaire_id=49')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
