#import unittest
#import json
#import http.client as httplib
#import urllib.parse as urllib
#from conf import httpserver
#from conf import httpport

#conn = httplib.HTTPConnection(httpserver, httpport)
#header = {"Content-type": "application/x-www-form-urlencoded"}

#class TestUser(unittest.TestCase):

#    def test_checkuserexist1(self): 
#        global conn
#        conn.request('GET', '/v1/user/signup/?username=aaaa')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
#        
#    def test_checkuserexist2(self): 
#        global conn
#        conn.request('GET', '/v1/user/signup/?username=bzj1')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertFalse(data["infostatus"])

#     def test_getsecretquestions(self): 
#        global conn
#        conn.request('GET', '/v1/user/secret/questions/')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])   
#    


#    def test_adduser1(self):
#        global conn
#        global header
#        params = {"username": "hello",
#                  "password": "123123",
#                  "security_quetion_id":"2",
#                  "security_answer":"2000-01-01"}
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/user/signup/', params, header)
#        data1 = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data1)
#        self.assertTrue(data1["infostatus"])
#       
#    def test_adduser2(self):
#        global conn
#        global header
#        params = {"username": "bai_charming",
#                  "password": "long",
#                  "security_quetion_id":"1",
#                  "security_answer":"24"}
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/user/signup/', params, header)
#        data1 = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data1)
#        self.assertTrue(data1["infostatus"])
#        
#    def test_adduser3(self):
#        global conn
#        global header
#        params = {"username": "张三",
#                  "password": "min",
#                  "security_quetion_id":"2",
#                  "security_answer":"1990-01-02"}
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/user/signup/', params, header)
#        data1 = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data1)
#        self.assertFalse(data1["infostatus"])
#        
#    def test_checklogin1(self):
#        global conn
#        global header
#        params = {"username": "long",
#                  "password": "long"}
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/user/login/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
#     
#    def test_checklogin2(self):
#        global conn
#        global header
#        params = {"username": "bai_charming",
#                  "password": "bai"}
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/user/login/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertFalse(data["infostatus"])
#       
#    def test_getidbyname(self):
#        global conn
#        conn.request('GET', '/v1/username/userid/?user_name=wys')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_tokendelete(self):
#        global conn
#        conn.request('GET', '/v1/token/delete/?user_token=d17882c9-dd71-4b13-8e49-e7f0e62e905a')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_showquestion01(self):
#        global conn
#        conn.request('GET', '/v1/user/show/question/?user_name=jack')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_showquestion02(self):
#        global conn
#        conn.request('GET', '/v1/user/show/question/?user_name=min')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_checksecurity01(self):
#        global conn
#        conn.request('GET', '/v1/user/check/security/?user_name=min&security_answer=1990-01-02')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])


#    def test_checksecurity02(self):
#        global conn
#        conn.request('GET', '/v1/user/check/security/?user_name=jack&security_answer=2000-01-02 ')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#        
#    def test_findpassword01(self):
#        global conn
#        global header
#        params = {
#                  "user_name":"jack",
#                  "user_password":111111
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/user/find/password/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"]) 


#        
#    def test_findpassword02(self):
#        global conn
#        global header
#        params = {
#                  "user_name":"wang",
#                  "user_password":111111
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/user/find/password/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"]) 

#    def test_checkoldpassword01(self):
#        global conn
#        conn.request('GET', '/v1/user/check/oldpassword/?usertoken=d17882c9-dd71-4b13-8e49-e7f0e62e905a&user_oldpassword=111111 ')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_checkoldpassword02(self):
#        global conn
#        conn.request('GET', '/v1/user/check/oldpassword/?usertoken=d17882c9-dd71-4b13-8e49-e7f0e62e905a&user_oldpassword=123456 ')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
#       
#        
#    def test_modifypassword01(self):
#        global conn
#        global header
#        params = {
#                  "usertoken":"d17882c9-dd71-4b13-8e49-e7f0e62e905a",
#                  "user_oldpassword":111111,
#                  "user_newpassword":123456
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/user/modify/password/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"]) 
#        
#    def test_modifypassword02(self):
#        global conn
#        global header
#        params = {
#                  "usertoken":"d17882c9-dd71-4b13-8e49-e7f0e62e905a",
#                  "user_oldpassword":112111,
#                  "user_newpassword":123456
#                  }
#        params = urllib.urlencode(params)
#        conn.request('POST', '/v1/user/modify/password/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"]) 

#    def test_showusername01(self):
#        global conn
#        conn.request('GET', '/v1/show/user/name/?usertoken=d17882c9-dd71-4b13-8e49-e7f0e62e905a')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])        


#    def test_showusername02(self):
#        global conn
#        conn.request('GET', '/v1/show/user/name/?usertoken=e418650e-8330-4426-82ff-178c70e8af82')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#    def test_getnamebytoken(self):
#        global conn
#        conn.request('GET', '/v1/token/username/?user_token=d17882c9-dd71-4b13-8e49-e7f0e62e905a')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
