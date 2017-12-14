#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import   urllib.request

"""
#删除文件
import   os,sys
print(os.getcwd())
print("开始删除文件!!!".center(80,"*"))
for  filel_line  in  range(1,100):
	filename=str(filel_line)+".html"
	if os.path.exists(filename):
		os.remove(filename)
	else:
		print("The {0} is  not  exists!".format(filename))
print("删除文件完成!!!".center(80,"@"))
"""
"""
#读取网页内容 写入文件方法1
url_list=["http://www.bundcredit.com","http://www.baidu.com","http://www.winnerlook.com","http://www.winnertoke.com"]
for  urlinfo  in url_list:
    file=urllib.request.urlopen(urlinfo)
    data=file.read()
    with  open(str(urlinfo).split(".")[1]+".html","wb") as fileinfo:
        fileinfo.write(data)
#读取网页内容 写入文件方法2 
for  fileline  in  range(1,10000):
    filename=urllib.request.urlretrieve("http://www.bundcredit.com",filename=str(fileline)+".html")
"""
"""
#模拟浏览器-Headers属性1
url="http://www.bundcredit.com"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
for   eachnum in  range(1,10000):
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	data = opener.open(url).read()
	with  open(str(eachnum)+".html", "wb") as fileinfo:
		fileinfo.write(data)

#模拟浏览器—Headers属性2
url="https://uat.bundcredit.com/frontend/login"
req=urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
data=urllib.request.urlopen(req).read()
print(data)
with  open(url.split(".")[1]+".html","wb") as scrapyfile:
	scrapyfile.write(data)
"""
def user_proxy(proxy_add,url):
	import urllib.request
	proxy=urllib.request.ProxyHandler({'http':proxy_add})
	opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)
	data=urllib.request.urlopen(url).read()
	return  data
proxy_addr="202.202.90.20:8080"
data=user_proxy(proxy_addr,"http://www.bundcredit.com")