#!/usr/bin/env python
#-*-coding:utf8-*-
import  psutil,socket
hostName=socket.gethostname()#获取主机名
localUser=psutil.users()[0][0]#获取本地的用户名
localIpaddr=psutil.net_if_addrs()["以太网"][1][1]
print("The computer  info is: ".center(80,"*"))
print("""The computer Hostname is: %s 
The  computer LocalUser is: %s 
The  computer LocalIpaddr is: %s"""
     %(hostName,localUser,localIpaddr))
# 磁盘信息
print("磁盘信息如下:".center(80,"*"))
for  hostDisk  in psutil.disk_partitions():
    print(hostDisk)
MN=psutil.disk_io_counters()
print(MN)

print("磁盘读写如下:".center(80,"*"))
print("""Read_count:{0}
Write_count:{1}
Read_bytes:{2}
Write_bytes:{3}
Read_time:{4}
Write_time:{5}""".format(psutil.disk_io_counters()[0],
                         psutil.disk_io_counters()[1],
                         psutil.disk_io_counters()[2],
                         psutil.disk_io_counters()[3],
                         psutil.disk_io_counters()[4],
                         psutil.disk_io_counters()[5]))