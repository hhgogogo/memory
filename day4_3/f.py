#!/usr/bin/env python
#_*_ coding:utf-8 -*-

import getpass

username= input("name:")

password = getpass.getpass("请输入密码:")

if username == "tom" and password == "123":
    print("login")
else:
    print("bed")