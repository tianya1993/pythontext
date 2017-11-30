#!/usr/bin/env python
#-*-coding:utf-8-*-
#!/usr/bin/env python
#-*-coding:utf-8-*-
import  os
os.chdir("D:/Apache/")
file_list = os.listdir()
file_name_list=[]
if os.path.exists("E:/pythontext/Devpython/deal_file/file_count.txt"):
    os.remove("E:/pythontext/Devpython/deal_file/file_count.txt")
for eachline in  sorted(file_list,key=lambda x:(int(x.split(".")[0]),int(x.split(".")[0])+1)):
    with open(eachline,"r",encoding=("utf-8")) as  source_file:
        file_name_list.append(source_file.read())
for eachlines in file_name_list:
    with open("E:/pythontext/Devpython/deal_file/file_count.txt","a",encoding="utf-8")  as    dest_file:
        dest_file.write("\n"+eachlines) #
