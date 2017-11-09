#!/usr/bin/env python
#-*-conding:utf8-*-
"""
def   Printtype(x):
    print("%s type is:%s" % (x, type(x)))
List=[]
Tuple=1,3,4,56,6,8
String=""
Dict={}
Printtype(List)
Printtype(Tuple)
Printtype(String)
Printtype(Dict)

s= [x*10  for   x in range(10)] #列表生成
print(s)

list2=[]
for   i  in range(10):
    list2.append(i*10)
print(list2)

"""
class Student:
    def  __init__(self,name,address,phone,*xargs,**xarg):
        """类变量"""
        self.name = name
        self.address = address
        self.phone = phone
        self.xargs = xargs
        self.xarg = xarg
    def  turn(self):
        new_address=self.address.title()
        return  new_address
    def show(self):
        """用{}格式化输出 缺点对变量的位置要求严格"""
        print("Name:{},Address:{},Tell:{},Xargs:{},Xarg{}".format(self.name,
               self.address,self.phone,self.xargs,self.xarg))

    def  showtype(self):
        """输出实例化的对象类型"""
        print("%s  type is:%s\n %s  type is:%s\n %s type is:%s\n %s type is:%s\n %s type is:%s\n"
              %(self.name,type(self.name),
            self.address,type(self.address),self.phone,type(self.phone),self.xargs,type(self.xargs),
        self.xarg,type(self.xarg)))
        print("{0} type is:{1}\n{2} type is:{3}\n{4} type is:{5}\n{6} type is:{7}\n{8} type is:{9}\n".format(
        self.name,type(self.name),self.address,type(self.address),self.phone,
        type(self.phone),self.xargs,type(self.xargs),self.xarg, type(self.xarg)
            )
                )
    def printinfo(self):
        print("{0}is lived{1}".format( self.name,self.address))

MySQL=Student("student","beijing","13830990518","北京","上海",age="12",job="devops")
MySQL.show()
MySQL.turn()
print(MySQL.turn())
MySQL.showtype()

backup=Student("DBA","henan","110")
backup.showtype()
backup.show()
backup.printinfo()
print(backup)