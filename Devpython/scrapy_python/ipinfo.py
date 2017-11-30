#!/usr/bin/env python
#-*-coding:utf-8-*-
import  urllib.request
import  json
url="http://ip.taobao.com/service/getIpInfo.php?ip=101.95.165.34"
data=urllib.request.urlopen(url)
datadict=json.load(data)
print(datadict)
print(datadict["data"]["country"])