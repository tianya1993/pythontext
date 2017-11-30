#!/usr/bin/env python
#-*-coding:utf8-*-
import  paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.1.4.20",port=22,username="root",password="p@ssw0rd")
stdin,stdout,stderr = ssh.exec_command('lsof  -i:3306')
result=stdout.read().decode("utf-8")
ssh.close()
print(result)