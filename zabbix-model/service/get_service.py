import json
import sys

def services(zapi):
    print("get services")
    item_dict = {}
    for h in zapi.service.get(output="extend"):
        print('----------------------')
        print(h['name'])
        
        item_dict['serviceid'] = h['serviceid']
        item_dict['name'] = h['name']

        # sla enable if return 1
        item_dict['showsla'] = h['showsla']

        # SLA percentage that is acceptable for this service; used for reporting
        item_dict['goodsla'] = h['goodsla']
        
        item_dict['serviceid'] = h['serviceid']
        
    return item_dict
