#!/usr/bin/env python
#-*-coding:utf8-*-
"""
分析Nginx等Web应用访问IP信息 并将其访问数量从大到小排序
"""
ip_list=[] #定义空列表 所有的访问IP放置在该列表中
ip_count={}#定义一个空字典 将IP和访问的次数放置到该字典中
with  open("D:/portal_ssl.access.log","r",encoding="utf-8")  as ngfile: #打开日志文件
    for line in   ngfile:
        #print(line.split())  调试信息
        ip_list.append(line.split()[0]) #用split分割字符串获取到列表line.split()[0] 每行的IP地址
for count in set(ip_list):   #将ip_list去重
    ip_number=ip_list.count(count)  #统计每个IP出现的次数
    ip_count.setdefault(count,ip_number) #将IP以及数量更新到字典
ip_count_new=sorted(ip_count.items(),key=lambda d:d[1],reverse=True) #使用lambda函数 对其重新排序构建新字典
for eachip  in ip_count_new:
    print(eachip)
print(len(ip_count_new))

