# !/usr/bin/python
# -*- coding:utf-8 -*-
import re
#import datetime
#import time
#import MySQLdb as mdb
import json
import urllib.request
import sys
#sys.setdefaultencoding( "utf-8" )
#log = "/root/access_" + (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d') + ".log"
line = open("nginx_access.log", 'r',encoding="utf8")
#con = mdb.connect('localhost', '', '', 'database', charset="utf8")
#cur = con.cursor()

try:
    ip_list = []
    for each_line in line:
        ip_list.append(each_line.split()[0])


    for  ip in set(ip_list):
        API = "http://ip.ws.126.net/ipquery?ip=" + ip
        #jsondata = json.loads(urllib.urlopen(API).read())
        urlinfo=urllib.request.urlopen(API).read().decode('gbk').encode('utf-8')
        print(urlinfo)
        #jsondata = json.loads(urllib.request.urlopen(API))
        #address = jsondata['data']['country'] + jsondata['data']['region'] + jsondata['data']['city'] + jsondata['data']['isp']
        print(ip,API)
finally:
    line.close()

"""       time = matchObj.group(2)
        method = matchObj.group(3)
        request = matchObj.group(4)
        status = int(matchObj.group(6))
        bytesSent = int(matchObj.group(7))
        request_time = float(matchObj.group(8))
        refer = matchObj.group(9)
        agent = matchObj.group(10)
        #cur.execute('insert into nginx_access_log values("%s","%s","%s","%s","%s",%d,%d,%f,"%s","%s")' % (
        #ip, address, time, method, request, status, bytesSent, request_time, refer, agent))
        print("%s,%s,%s,%s,%s,%d,%d,%f,%s,%s" % (ip, address, time, method, request, status, bytesSent, request_time, refer, agent))
"""

    #cur.close()
