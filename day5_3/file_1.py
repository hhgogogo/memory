#!/usr/bin/env python
#_*_ coding:utf-8 -*-
__author__ = 'SmartGo'

#取内存总量
f = open('/proc/meminfo','r')

for lines in f:
    if lines.startswith("MemTotal:"):       #以MemTotal:开头的
        memtotal = int(lines.split()[1]) / 1024 /1024
    if lines.startswith("MemFree:"):
        memfree = int(lines.split()[1]) / 1024 /1024
        break
print("Userd:%.2fG - %.2fG = %.2fG"%(memtotal ,memfree,memtotal - memfree))