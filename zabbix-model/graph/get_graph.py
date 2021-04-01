def graphs(zapi,host_id):
    graphimg_list = []
    print("monitor host id")
    for h in zapi.graph.get(output="extend",hostids=host_id):
        graphimg_dict = {}
        img_url="http://zabbix/zabbix/chart2.php?graphid={id}&width=640&period=86400".format(id=h['graphid'])
        graphimg_dict['graph_id'] = h['graphid']
        graphimg_dict['name'] = h['name']
        graphimg_dict['img_url'] = img_url
        graphimg_list.append(graphimg_dict)
    return graphimg_list