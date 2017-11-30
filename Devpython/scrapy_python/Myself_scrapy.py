#!/usr/bin/env python
#-*-coding:utf-8-*-
import  urllib.request
"""
url="https://uat.bundcredit.com/frontend/login"
req=urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
data=urllib.request.urlopen(req).read()
print(data)
"""
"""
url = "https://uat.bundcredit.com/frontend/login"
heards = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
opener=urllib.request.build_opener()
opener.addheaders=[heards]
data=opener.open(url).read()
print(data)
"""
"""
file=urllib.request.urlretrieve("http://www.baidu.com","index.html")
url="http://www.baidu.com"
req=urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
data=urllib.request.urlopen(req).read()
print(data)
"""
url="http://www.baidu.com"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
print(data)
