#!/usr/bin/env python
#-*-coding:utf8-*-
Phone_list=[]
with   open("C:/Users/CJ/Desktop/cellphone.txt","r") as  f:
    for   phone  in f.readlines():
        Phone_list.append(phone)
print(len(Phone_list))

Phone_set=set(Phone_list)
Phone_list_after=list(Phone_set)
with open("C:/Users/CJ/Desktop/cellphone2.txt","w")  as  flie:
    flie.writelines(Phone_list_after)
print(len(Phone_list_after))