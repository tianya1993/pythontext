#!/usr/bin/env python
#-*-conding:utf8-*-
while True:
    try:
        x=int(input("Please enter a  number:"))
        print(x)
        break
    except ValueError :
        print("input  value  error")