def problems(zapi):
    problem_list = []
    print("host problems")
    for host in zapi.host.get(output="extend"):
        print("For this host id "+host['hostid'])
        hostprob_dict = {}
        for h in zapi.problem.get(output="extend",hostids=host['hostid']):
            hostprob_dict['hostid'] = host['hostid']
            hostprob_dict['name'] = h['name']
            ack_count = h['acknowledged']
            hostprob_dict['ack_message'] = h['acknowledges'][ack_count]['message']
            hostprob_dict['severity'] = host['severity']
        problem_list.append(hostprob_dict)
    return problem_list
