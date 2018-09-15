#!/usr/bin/env python
#_*_ coding:utf-8 -*-

info = {}

name = input("pls enter your name:")
age = int(input("please enter your age:"))

info ["name"] =name
info ["age"] = age

#for i in info.items():
#    print(i)

#print('finish!!!')

for k,v in info.items():
    print(k,v)

#for k,v in info.items():
#    print("%s--->%s" %(k,v))