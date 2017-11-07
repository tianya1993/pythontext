#!/usr/bin/env python
#-*-coding:utf8-*-
class   Student:
    def __init__(self,name,grade,sex,address,phone):
        self.name=name
        self.grade=grade
        self.sex=sex
        self.address=address
        self.phone=phone

    def introduce(self):
        print("Hi I'm"+ self.name)
        print("my grade is:"+str(self.grade))
        print("Name is:{0}\tAge:{1}\tSex:{2}\tAddress:{3}\tPhone:{4}".format(self.name,self.grade,self.sex,self.address,self.phone))
    def improve(self,amount):
        self.grade=self.grade+ amount
jim=Student("docker",88,"男","北京东路","13830990518")
jim.introduce()
jim.improve(10)
jim.introduce()

mysql=Student("mysql",90,"女","上海市","13220880518")
mysql.introduce()