#!/usr/bin/env python
#-*-coding:utf-8-*-
"""输出 1-100 内的所有奇数"""
x=0
while True:
    if x == 100:
        break
    x +=1
    #if 0 =x %2
    if 0 !=x %2:
        print(x)
