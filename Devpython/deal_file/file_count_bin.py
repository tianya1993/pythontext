#!/usr/bin/env python
#-*-coding:utf-8-*-
#!/usr/bin/env python
#-*-coding:utf-8-*-
import  os
os.chdir("D:/Apache/")
file_list = os.listdir()
for eachline in  file_list:
    with open(eachline,"rb") as  source_file:
        with open("E:/pythontext/Devpython/deal_file/file_count.jpg","ab")  as    dest_file:
            dest_file.write(source_file.read()) #
