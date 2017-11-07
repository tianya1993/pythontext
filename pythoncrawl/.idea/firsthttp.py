# !/usr/bin/env python
# _*_coding:utf-8_*_
import   getpass
print('----***字符串格式化输出***----')
name = input("input your name:")
age = input("input your age:")
job = input("input your job:")
salary = input("input your salary:")

info3 = """ -------******info of {_name}-------******
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}

""".format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)
print(info3)

info4 = """ -------******info of {0} 该方式适合变量少的情况括号是花括号-------******
name:{0}
age:{1}
job:{2}
salary:{3}

""".format(name, age, job, salary
           )
print(info4)