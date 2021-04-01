import json
import sys

def servicesla(zapi):
    print("get services sla")
    servicesla_list = []
    for service in zapi.service.get(output="extend"):
        sla_dict = {}
        for h in zapi.service.getsla(output="extend",serviceids=service['serviceid']):
            sla_dict['service_id'] = service['serviceid']
            sla_dict['name'] = service['name']
            sla_dict['sla_threshold'] = service['goodsla']
                # for attr in h[0]:
                # sla_dict['actual_sla'] = h[0]
                # print("the status is "+h[0][0][0])
                # sla_dict['ok_time'] = h['serviceid']['sla']['okTime']
                # sla_dict['problem_time'] = h['serviceid']['sla']['problemTime']
                # sla_dict['down_time'] = h['serviceid']['sla']['downtimeTime']
        servicesla_list.append(sla_dict)
    return servicesla_list
