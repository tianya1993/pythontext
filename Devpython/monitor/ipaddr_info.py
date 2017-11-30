# !/usr/bin/python
# -*- coding:utf-8 -*-
import  json
import  urllib.request
import  pymysql
conne=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="p@ssw0rd",db="ip_pool",charset="utf8mb4")
curor=conne.cursor()
#print(curor.execute("show tables"))
SQL="""insert  into  ipinfo(`ip_address`,`country`,`country_id`,`area`,`region`,`region_id`,`city`,`city_id`,`isp`,`isp_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
ip_souce_list=[]
with open("D:/portal_ssl.access.log","r",encoding="utf-8") as  source_file:
    for  eachip  in  source_file.readlines():
        ip_souce_list.append(eachip.split(" ")[0])
    print(set(ip_souce_list))
#ip_souce_list=['58.210.143.102', '139.226.51.148', '114.80.240.184', '101.95.165.34',   '183.129.232.234', '124.207.44.178']
for dest_ip in set(ip_souce_list):
    url="http://ip.taobao.com/service/getIpInfo.php?ip="
    httpinfo=urllib.request.urlopen(url+dest_ip)
    sourcedata=httpinfo.read()
    destdata=json.loads(sourcedata)
    print(dest_ip,destdata["data"])
    curor.execute(SQL,(destdata["data"]["ip"],
                       destdata["data"]["country"],
                       destdata["data"]["country_id"],
                       destdata["data"]["area"],
                       destdata["data"]["region"],
                       destdata["data"]["region_id"],
                       destdata["data"]["city"],
                       destdata["data"]["city_id"],
                       destdata["data"]["isp"],
                       destdata["data"]["isp_id"],))
    conne.commit()
conne.close()

