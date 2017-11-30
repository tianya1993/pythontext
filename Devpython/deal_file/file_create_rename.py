#!/usr/bin/env python
#-*-coding:utf-8-*-
import  os,sys
import time,datetime
now= datetime.datetime.now()
print(now.time())
print()
os.chdir("D:/Apache/")
for i in  range(1,1000):

    with open(str(i)+'.txt','w',encoding='utf-8') as file:
        file.write('{} 是最吉利的数字'.format(i))

    ##os.remove(str(i)+".txt")
        """
filelist=os.listdir("")
for  filename  in filelist:
    #print(filename)
    if os.path.exists("D:/Apache/"+filename):
        #os.rename("D:/Apache/"+filename,"D:/Apache/"+filename.split(".")[0]+str(now.time()).split(".")[1] +".html")

        os.remove("D:/Apache/"+filename)
        #print(filename.split(".")[0])
    else:
        print("The {file} is not  exist".format(file=filename))
"""