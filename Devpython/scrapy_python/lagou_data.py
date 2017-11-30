#!/usr/bin/env python
#-*-coding:utf-8-*-
import  urllib.request
#import   request
url="https://www.lagou.com/jobs/list_python?px=default&city=%E5%85%A8%E5%9B%BD#filterBox"
#data=urllib.request.urlopen(url)
req=urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
data=urllib.request.urlopen(req)
print(data.read().decode("utf-8"))