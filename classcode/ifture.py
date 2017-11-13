#!/usr/bin/env python
#-*-coding:utf8-*-
"""请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
 print(L2)
['hello', 'world', 'apple']
 """

""" 
L = ['Hello', 'World', 18, 'Apple', None,"66"]
#L=["list",6,8,"apple","docker","66"]

L2=[]
for index in L:
    if  isinstance(index,str):
        L2.append(index.lower())
    else:
        continue
print(L2)
"""
L1 = ['Hello', 'World', 18, 'Apple', None,"66",[18, 'Apple', None,"66"]]
#L2 = [x**2 for x in L1 if isinstance(x, (str))]
#print(L2)
L3=[x+"1"  for x  in L1 if   isinstance(x,(str))]
print(L3)
