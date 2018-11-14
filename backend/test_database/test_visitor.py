##! /usr/bin/env python
##coding=utf-8
#import urllib
#import unittest
#import json
#import http.client as httplib
#import urllib.parse as urllib
#from conf import httpserver
#from conf import httpport

#conn = httplib.HTTPConnection(httpserver, httpport)
#header = {"Content-type": "application/x-www-form-urlencoded"}

#class TestVisitor(unittest.TestCase):

#    def test_openlink(self): 
#        global conn
#        global header
#        url = '/v1/visitor/openlink/?questionnaire_link=http://www.questionnaire.com/s/number03'
#        conn.request('GET', url)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_fillin(self):
#        global conn
#        global header
#        params = {"questionnaire_id":1,
#                  "options":[{"subject_id":24,"option_id":42},{"subject_id":22,"interlocution_content":"没什么建议"}]
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/visitor/fillin/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_alarm(self):
#        global conn
#        global header
#        params = {"questionnaire_id":1
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/visitor/alarm', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
