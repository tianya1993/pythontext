#!/usr/bin/env python
#-*-coding:utf8-*-
with  open("pythonfile.txt","r",encoding="utf8") as  filename:
    #data=filename.read()
    #print(data)
    data2=filename.read(5)
    print(data2)
    #with open("write.txt","w",encoding="utf8") as  filewire: