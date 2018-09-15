#!/usr/bin/env python
#_*_ coding:utf-8 -*-
__author__ = 'SmartGo'

x = ''
prompt = """1，矿泉水
2，可口可乐
请使用（1，2）："""

while not x:
    print("请选择以下菜单内容:")
    x = input(prompt)
    if x == '1':
        print("没水")
    elif x == '2':
        print("没有，滚！")