import json
import sys

def host_id(zapi):
    hostid_list = []
    print("monitor host id")
    for h in zapi.host.get(output="extend"):
        host_dict = {}
        print(h['hostid'])
        host_dict['hostid'] = h['hostid']
        host_dict['name'] = h['host']
        hostid_list.append(host_dict)
    return hostid_list