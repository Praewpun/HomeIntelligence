import json
import sys

def host_id(zapi):
    hostid_list = []
    print("monitor host id")
    for h in zapi.host.get(output="extend"):
        print(h['hostid'])
        hostid_list.append(h['hostid'])
    return hostid_list




