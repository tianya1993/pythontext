#!/usr/bin/env python
#-*-coding:utf8-*-
import   urllib.request
import  re
url="http://www.bundcredit.com"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0")
opener = urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
with  open( "1.html", "wb") as fileinfo:
    fileinfo.write(data)



"""
url_list=["http://www.bundcredit.com","http://www.baidu.com","http://www.winnerlook.com","http://www.winnertoke.com"]
for  urlinfo  in url_list:
    file=urllib.request.urlopen(urlinfo)
    data=file.read()
#print(os.getcwd())
    print(file.getcode())
    print(file.geturl())
#print(data)
    with  open(str(urlinfo).split(".")[1]+".html","wb") as fileinfo:
        fileinfo.write(data)
"""
with  open( "1.html", "wb") as fileinfo:
    fileinfo.write(data)

"""
for fileline  in  range(1,100):
    filename=urllib.request.urlretrieve("http://www.cniao5.com/course/sz.html",filename=str(fileline)+".html")

"""