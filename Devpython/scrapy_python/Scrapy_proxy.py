#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib.request
import random
url = 'http://www.winnerlook.com'
iplist = ['202.202.90.20:8080','119.36.92.47:80','1.83.102.99:9000']
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url,data=None,timeout=500)
html = response.read()
print(html)
