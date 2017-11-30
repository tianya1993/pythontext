#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import  urllib.request
#file=urllib.request.urlretrieve("http://www.baidu.com","baidu.html")
url="http://www.baidu.com"
#file=urllib.request.urlopen(url)
req=urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
data=urllib.request.urlopen(req).read()
print(data)
with open("baidu2.html","wb") as  filename:
	filename.write(data)