#!/usr/bin/env python
#_*_ coding:utf-8 -*-
__author__ = 'SmartGo'

def fun(num):
    try:
        if type(int(num)) == type(1):
            print("请输入数字")
    except ValueError as e:
            print("输入的不是纯数字")
    return num