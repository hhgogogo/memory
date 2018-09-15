#!/usr/bin/env python
#_*_ coding:utf-8 -*-
__author__ = 'SmartGo'
import getpass

username = input("请输入名:")
password = getpass.getpass("输入密码:")
sb = 0
while True:
    if username =='tom' and password =='123':
        print("登陆成功")
        break
    else:
        sb = sb + 1
        print("失败%s次" %sb)
        if sb == 3:
            print("登陆失败")
            break
    username = input("name:")
    password = input("passwd:")
