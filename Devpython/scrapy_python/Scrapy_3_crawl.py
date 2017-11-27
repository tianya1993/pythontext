#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import  urllib.request
#file=urllib.request.urlretrieve("http://www.baidu.com","baidu.html")
url="http://www.baidu.com"
file=urllib.request.urlopen(url)
data=file.read()
print(data)
with open("baidu2.html","wb") as  filename:
	filename.write(data)