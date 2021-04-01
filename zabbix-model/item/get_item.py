import json
import sys

def item_id(zapi):
    item_list = []
    print("monitor host id")
    for host in zapi.host.get(output="extend"):
        print("For this host id "+host['hostid'])
        item_dict = {}
        for h in zapi.item.get(output="extend",hostids=host['hostid']):
            print('----------------------')
            print("hostid is "+h['hostid'])
            print(h['name'])
            
            if host['hostid'] == h['hostid']:
                item_dict['host_id'] = h['hostid']
            if 'Interface Killer e2200 Gigabit Ethernet Controller (NDIS 6.30)(Ethernet): Bits sent' == h['name']:
                item_dict['Interface killer: Bits sent'] = h['lastvalue']
            if 'Interface Killer e2200 Gigabit Ethernet Controller (NDIS 6.30)(Ethernet): Bits received' == h['name']:
                item_dict['Interface killer: Bit received'] = h['lastvalue']
            if '/var/lib/mysql: Total space' == h['name']:
                item_dict['mysql total space'] = h['lastvalue']
            if '/: Used space' == h['name']:
                item_dict['Total used space in host'] = h['lastvalue']
            if '/: Space utilization' == h['name']:
                item_dict['Space Utilization'] = h['lastvalue']
            if 'Used memory' == h['name']:
                item_dict['Used memory'] = h['lastvalue']
            if 'Total memory' == h['name']:
                item_dict['Total memory'] = h['lastvalue']
            if 'CPU interrupt time' == h['name']:
                item_dict['CPU interrupt time'] = h['lastvalue']
            if 'CPU privileged time' == h['name']:
                item_dict['CPU privileged time'] = h['lastvalue']
            if 'CPU user time' == h['name']:
                item_dict['CPU user time'] = h['lastvalue']
            if 'Context switches per second' == h['name']:
                item_dict['Context switches per second'] = h['lastvalue']
            if 'CPU utilization' == h['name']:
                item_dict['CPU utilization'] = h['lastvalue']
            if 'Free swap space' == h['name']:
                item_dict['Free swap space'] = h['lastvalue']
            if 'Total swap space' == h['name']:
                item_dict['Total swap space'] = h['lastvalue']
            if 'Uptime' == h['name']:
                item_dict['Uptime'] = h['lastvalue']
            if 'Used memory' == h['name']:
                item_dict['Used memory'] = h['lastvalue']
            if 'Memory utilization' == h['name']:
                item_dict['Memory utilization'] = h['lastvalue']
            if 'System description' == h['name']:
                item_dict['System description'] = h['lastvalue']
            if 'Total memory' == h['name']:
                item_dict['Total memory'] = h['lastvalue']
            if 'Host name of Zabbix agent running' == h['name']:
                item_dict['Host name of Zabbix agent running'] = h['lastvalue']
            if 'Number of processes' == h['name']:
                item_dict['Number of processes'] = h['lastvalue']
            if 'Operating system architecture' == h['name']:
                item_dict['Operating system architecture'] = h['lastvalue']
            if 'Interface eth0: Bits received' == h['name']:
                item_dict['Interface eth0: Bits received'] = h['lastvalue']
            if 'Interface eth0: Bits sent' == h['name']:
                item_dict['Interface eth0: Bits sent'] = h['lastvalue']

            if '0 C:: Disk utilization' == h['name']:
                item_dict['Disk C Utilization'] = h['lastvalue']
            if '1 D:: Disk utilization' == h['name']:
                item_dict['Disk D Utilization'] = h['lastvalue']
            if '0 C:: Average disk read queue length' == h['name']:
                item_dict['Disk C Average disk read queue length'] = h['lastvalue']
            if '1 D:: Average disk read queue length' == h['name']:
                item_dict['Disk D Average disk read queue length'] = h['lastvalue']
            if '0 C:: Average disk write queue length' == h['name']:
                item_dict['Disk D Average disk write queue length'] = h['lastvalue']
            if '1 D:: Average disk write queue length' == h['name']:
                item_dict['Disk D Average disk write queue length'] = h['lastvalue']
            if '0 C:: Disk read request avg waiting time' == h['name']:
                item_dict['Disk C Read request avg waiting time'] = h['lastvalue']
            if '1 D:: Disk read request avg waiting time' == h['name']:
                item_dict['Disk D Read request avg waiting time'] = h['lastvalue']
            if '0 C:: Disk write request avg waiting time' == h['name']:
                item_dict['Disk C Write request avg waiting time'] = h['lastvalue']
            if '1 D:: Disk write request avg waiting time' == h['name']:
                item_dict['Disk D Write request avg waiting time'] = h['lastvalue']
            if '0 C:: Disk average queue size (avgqu-sz)' == h['name']:
                item_dict['Disk C Average queue size (avgqu-sz)'] = h['lastvalue']
            if '1 D:: Disk average queue size (avgqu-sz)' == h['name']:
                item_dict['Disk D Average queue size (avgqu-sz)'] = h['lastvalue']
            if '0 C:: Disk read rate' == h['name']:
                item_dict['Disk C Read rate'] = h['lastvalue']
            if '1 D:: Disk read rate' == h['name']:
                item_dict['Disk D Read rate'] = h['lastvalue']
            if '0 C:: Disk write rate' == h['name']:
                item_dict['Disk C Write rate'] = h['lastvalue']
            if '1 D:: Disk write rate' == h['name']:
                item_dict['Disk D Write rate'] = h['lastvalue']

            if 'C:: Total space' == h['name']:
                item_dict['Disk C Total space'] = h['lastvalue']
            if 'D:: Total space' == h['name']:
                item_dict['Disk D Total space'] = h['lastvalue']
            if 'C:: Used space' == h['name']:
                item_dict['Disk C Used space'] = h['lastvalue']
            if 'D:: Used space' == h['name']:
                item_dict['Disk D Used space'] = h['lastvalue']

        item_list.append(item_dict)
    return item_list

def item_hostid(zapi,host_id):
    print("monitor host id")
    item_dict = {}
    for h in zapi.item.get(output="extend",hostids=host_id):
        print('----------------------')
        print("hostid is "+h['hostid'])
        print(h['name'])
        
        item_dict['host_id'] = h['hostid']
        if 'Interface Killer e2200 Gigabit Ethernet Controller (NDIS 6.30)(Ethernet): Bits sent' == h['name']:
            item_dict['Interface killer: Bits sent'] = h['lastvalue']
        if 'Interface Killer e2200 Gigabit Ethernet Controller (NDIS 6.30)(Ethernet): Bits received' == h['name']:
            item_dict['Interface killer: Bit received'] = h['lastvalue']
        if '/var/lib/mysql: Total space' == h['name']:
            item_dict['mysql total space'] = h['lastvalue']
        if '/: Used space' == h['name']:
            item_dict['Total used space in host'] = h['lastvalue']
        if '/: Space utilization' == h['name']:
            item_dict['Space Utilization'] = h['lastvalue']
        if 'Used memory' == h['name']:
            item_dict['Used memory'] = h['lastvalue']
        if 'Total memory' == h['name']:
            item_dict['Total memory'] = h['lastvalue']
        if 'CPU interrupt time' == h['name']:
            item_dict['CPU interrupt time'] = h['lastvalue']
        if 'CPU privileged time' == h['name']:
            item_dict['CPU privileged time'] = h['lastvalue']
        if 'CPU user time' == h['name']:
            item_dict['CPU user time'] = h['lastvalue']
        if 'Context switches per second' == h['name']:
            item_dict['Context switches per second'] = h['lastvalue']
        if 'CPU utilization' == h['name']:
            item_dict['CPU utilization'] = h['lastvalue']
        if 'Free swap space' == h['name']:
            item_dict['Free swap space'] = h['lastvalue']
        if 'Total swap space' == h['name']:
            item_dict['Total swap space'] = h['lastvalue']
        if 'Uptime' == h['name']:
            item_dict['Uptime'] = h['lastvalue']
        if 'Used memory' == h['name']:
            item_dict['Used memory'] = h['lastvalue']
        if 'Memory utilization' == h['name']:
            item_dict['Memory utilization'] = h['lastvalue']
        if 'System description' == h['name']:
            item_dict['System description'] = h['lastvalue']
        if 'Total memory' == h['name']:
            item_dict['Total memory'] = h['lastvalue']
        if 'Host name of Zabbix agent running' == h['name']:
            item_dict['Host name of Zabbix agent running'] = h['lastvalue']
        if 'Number of processes' == h['name']:
            item_dict['Number of processes'] = h['lastvalue']
        if 'Operating system architecture' == h['name']:
            item_dict['Operating system architecture'] = h['lastvalue']
        if 'Interface eth0: Bits received' == h['name']:
            item_dict['Interface eth0: Bits received'] = h['lastvalue']
        if 'Interface eth0: Bits sent' == h['name']:
            item_dict['Interface eth0: Bits sent'] = h['lastvalue']

        if '0 C:: Disk utilization' == h['name']:
            item_dict['Disk C Utilization'] = h['lastvalue']
        if '1 D:: Disk utilization' == h['name']:
            item_dict['Disk D Utilization'] = h['lastvalue']
        if '0 C:: Average disk read queue length' == h['name']:
            item_dict['Disk C Average disk read queue length'] = h['lastvalue']
        if '1 D:: Average disk read queue length' == h['name']:
            item_dict['Disk D Average disk read queue length'] = h['lastvalue']
        if '0 C:: Average disk write queue length' == h['name']:
            item_dict['Disk D Average disk write queue length'] = h['lastvalue']
        if '1 D:: Average disk write queue length' == h['name']:
            item_dict['Disk D Average disk write queue length'] = h['lastvalue']
        if '0 C:: Disk read request avg waiting time' == h['name']:
            item_dict['Disk C Read request avg waiting time'] = h['lastvalue']
        if '1 D:: Disk read request avg waiting time' == h['name']:
            item_dict['Disk D Read request avg waiting time'] = h['lastvalue']
        if '0 C:: Disk write request avg waiting time' == h['name']:
            item_dict['Disk C Write request avg waiting time'] = h['lastvalue']
        if '1 D:: Disk write request avg waiting time' == h['name']:
            item_dict['Disk D Write request avg waiting time'] = h['lastvalue']
        if '0 C:: Disk average queue size (avgqu-sz)' == h['name']:
            item_dict['Disk C Average queue size (avgqu-sz)'] = h['lastvalue']
        if '1 D:: Disk average queue size (avgqu-sz)' == h['name']:
            item_dict['Disk D Average queue size (avgqu-sz)'] = h['lastvalue']
        if '0 C:: Disk read rate' == h['name']:
            item_dict['Disk C Read rate'] = h['lastvalue']
        if '1 D:: Disk read rate' == h['name']:
            item_dict['Disk D Read rate'] = h['lastvalue']
        if '0 C:: Disk write rate' == h['name']:
            item_dict['Disk C Write rate'] = h['lastvalue']
        if '1 D:: Disk write rate' == h['name']:
            item_dict['Disk D Write rate'] = h['lastvalue']

        if 'C:: Total space' == h['name']:
            item_dict['Disk C Total space'] = h['lastvalue']
        if 'D:: Total space' == h['name']:
            item_dict['Disk D Total space'] = h['lastvalue']
        if 'C:: Used space' == h['name']:
            item_dict['Disk C Used space'] = h['lastvalue']
        if 'D:: Used space' == h['name']:
            item_dict['Disk D Used space'] = h['lastvalue']
    return item_dict



# host_id = zapi.host.get({"filter":{"host":host_name}})[0]["hostid"]