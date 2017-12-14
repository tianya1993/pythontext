#!/usr/bin/env python
#-*-coding:utf8-*-
# !/usr/bin/python
# -*- coding:utf-8 -*-
import  json
import  urllib.request
import  pymysql
import  time
import   psutil
import   socket



cpu_used=psutil.cpu_percent()
host_name=socket.gethostname()#获取主机名
host_ipadd=psutil.net_if_addrs()
ipList = socket.gethostbyname_ex(host_name)
print(ipList[2][2])
#print(host_ipadd)
memory_used=psutil.swap_memory()[1]
print(memory_used)

print(cpu_used)
conne=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="p@ssw0rd",db="ip_pool",charset="utf8mb4")
curor=conne.cursor()

SQL2="insert into ip_class(`date`,`ip`,`cpu`,`mem`,`io`,`disk`,`eth`)  values(%s,%s,%s,%s,%s,%s,%s)"
curor.execute(SQL2,( time.strftime("%Y-%m-%d %X", time.localtime()),'192.168.100.1','80','70','90','70','90'))
conne.commit()
