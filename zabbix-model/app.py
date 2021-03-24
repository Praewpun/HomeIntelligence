#  Use flask for route
import flask 
import requests
import json
import sys

from authenticate import *
from host.get_host import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def main_page():
    return "Hello"

@app.route("/zabbix/authenticate", methods=['GET', 'POST', 'PUT'])
def authenticate():
    auth_token = authenticate_zabbix().auth
    return json.dumps(auth_token)

@app.route("/zabbix/gethost")
def get_host():
    zapi = authenticate_zabbix()
    hostid_list  = host_id(zapi)
    return json.dumps(hostid_list)

@app.route("/zabbix/get")
def get_host():
    zapi = authenticate_zabbix()
    hostid_list  = host_id(zapi)
    return json.dumps(hostid_list)

app.run()