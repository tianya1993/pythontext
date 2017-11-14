#!/usr/bin/env python
#-*-coding:utf8-*-
class  Animal(object):
    def  __init__(self,name,age):
        self.name = name
        self.age = age
    def run():
        print("  %s is  runging!"%(self.name))
class Dog(Animal):
    def  __init__(self,name,age,color):#继承覆盖
        #super(Dog,self).__init__(name,age)#将相关参数传递给父类  新式类
        Animal.__init__(self,name,age) #经典类的用法
        self.color=color
    def run(self):
        print(" The {0} is {1}  runging".format(self.name,self.color))
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    def eat(self):
        print('Eating foods.')
dog = Dog("baidu",10,"blue")
dog.run()
dog.eat()

#cat = Cat()
#cat.run()
#cat.eat()