#!/usr/bin/env python
#-*-coding:utf-8-*-
import  re
pattern=re.compile("[a-zA-Z]+://[^\s]*[.com|.cn]")
string="src=http://yum.iqianyuee.com,https://www.bundcredit.com"
result=pattern.findall(string)
print(result)