from flask import Flask
from flask.ext import restful
from dapis.v1 import routedict as api_v1
from conf import httpserver
from conf import httpport
from orml import createtable

app = Flask(__name__)
api = restful.Api(app)
for k, v in api_v1.items():
    api.add_resource(k, v)

if __name__ == '__main__':
    print("dbserver started on http://" +
          str(httpserver) + ":" + str(httpport))
    app.run(host=httpserver, port=int(httpport), debug=True)
