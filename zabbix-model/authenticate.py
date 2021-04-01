import requests
import sys
import logging
from pyzabbix import ZabbixAPI
import json

# def authenticate_zabbix(username,password):
def authenticate_zabbix():
    # stream = logging.StreamHandler(sys.stdout)
    # stream.setLevel(logging.DEBUG)
    # log = logging.getLogger('pyzabbix')
    # log.addHandler(stream)
    # log.setLevel(logging.DEBUG)

    zapi = ZabbixAPI("http://192.168.1.30")
    # zapi.login(username,password)
    zapi.login("Admin","zabbix")
    print("The token is "+ zapi.auth)
    return zapi




