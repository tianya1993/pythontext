#!/usr/bin/env python
#-*-coding:utf8-*-

class Role:
    n=123  #类变量 保存在类内存中  在没实例化之前就可以调用
    name="linux"
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        #构造函数
        #在实例化时做一些类的初始化
        self.name = name #实例变量(属性) 作用域是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value=life_value
        self.money=money
    def show(self):
        pass

alex=Role("alex","DBA","123")
print(alex.name,alex.money)
print(Role.n)
print(Role.name)