#!/usr/bin/env python
#_*_ coding:utf-8 -*-
__author__ = 'SmartGo'

for i in range(1,10):
         for j in range(1,i+1):
             print("%s * %s = %s" %(j,i,i * j),end="  ")
         print()
