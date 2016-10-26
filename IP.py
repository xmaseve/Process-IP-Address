# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:47:42 2016

@author: Qi Yi
"""

import pandas as pd

ip1000 = pd.read_excel('C:\\Users\\Qi Yi\\Desktop\domain2ip-Insegment_IPs_1000-with-ips.xlsx')
ip300 = pd.read_excel('C:\\Users\\Qi Yi\\Desktop\domain2ip-Insegment_IPs_300.with-ips.xlsx')

IP1000 = ip1000["IP"]
IP300 = ip300["IP"]

IP1000 = IP1000.values.tolist()
IP300 = IP300.values.tolist()

def extract(data):
    start_ip = []
    end_ip = []
    length = []
    for row in data:
        row_list = str(row)
        row_list = row_list.split(",")
        leng = len(row_list)
        start = row_list[0]
        end = row_list[-1]
        start_ip.append(start)
        end_ip.append(end)
        length.append(leng)
    return start_ip, end_ip, length
    
start1000, end1000, length1000 = extract(IP1000)
start300, end300, length300 = extract(IP300)

ip1000["starting ip"] = start1000
ip1000["ending ip"] = end1000
ip1000["length"] = length1000

ip300["starting ip"] = start300
ip300["ending ip"] = end300
ip300["length"] = length300

ip1000.to_excel("C:\\Users\\Qi Yi\\Desktop\\domain2ip-Insegment_IPs_1000.xlsx") 
ip300.to_excel("C:\\Users\\Qi Yi\\Desktop\\domain2ip-Insegment_IPs_300.xlsx") 
    
