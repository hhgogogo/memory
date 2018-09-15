#!/usr/bin/env python
#_*_ coding:utf-8 -*-
__author__ = 'SmartGo'

l1=[1,2]


for i in range(8):
    l1.append(l1[-1] + l1[-2])
print(l1)