#!/usr/bin/env python
#-*-conding:utf8-*-
import random
checkcode = ''
for i in range(6):
    current = random.randrange(0,6)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print (checkcode)