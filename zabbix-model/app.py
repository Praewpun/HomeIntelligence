# Use flask for route
import flask 
import requests
import json
import sys

from authenticate import *
from host.get_host import *
from item.get_item import *
from service.get_service_sla import *
from service.get_service import *
from graph.get_graph import *

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

@app.route("/zabbix/getitem")
def get_stream():
    zapi = authenticate_zabbix()
    item_list  = item_id(zapi)
    return json.dumps(item_list)

@app.route("/zabbix/getitem/<int:host_id>")
def get_host_item(host_id):
    zapi = authenticate_zabbix()
    hostitem_list  = item_hostid(zapi,host_id)
    return json.dumps(hostitem_list)

@app.route("/zabbix/servicesla")
def get_servicesla():
    zapi = authenticate_zabbix()
    servicesla_list  = servicesla(zapi)
    return json.dumps(servicesla_list)

@app.route("/zabbix/service")
def get_service():
    zapi = authenticate_zabbix()
    services_list  = services(zapi)
    return json.dumps(services_list)

@app.route("/zabbix/getgraph/<int:host_id>")
def get_graph(host_id):
    zapi = authenticate_zabbix()
    hostgraph_list  = graphs(zapi,host_id)
    return json.dumps(hostgraph_list)


app.run()