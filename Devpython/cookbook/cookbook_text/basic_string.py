#!/usr/bin/env python
#-*-coding:utf8-*-
#Name=input("Please ")
class  Count(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #self.xargs=xargs
    def  add(self):
        return self.x +self.y
    def sub(self):
        return self.x - self.y
    def mult(self):
        return self.x * self.y
    def  divide(self):
        return self.x/self.y
    def   show (self):
        print("{0} : {1}  " .format(self.x,self.y))
num1=Count(3,5)
num1.add()
print(num1.add())
print(num1.sub())
print(num1.mult())
num1.show()