#!/usr/bin/env python
#_*_ coding:utf-8 -*-
__author__ = 'SmartGo'

l1 = [1,2]

num = int(input("num:"))

for i in range(num-2):
    l1.append(l1[-1]+l1[-2])

print(l1)