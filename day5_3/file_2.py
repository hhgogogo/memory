#!/usr/bin/env python
#_*_ coding:utf-8 -*-
__author__ = 'SmartGo'

s_file = '/usr/bin/ls'
d_file = '/home/sl'

s_obj_file = open(s_file,'rb')

d_obj_file = open(d_file,'wb')
buffer_size = 4096
while True:
    date = s_obj_file.readline(buffer_size)
    if not date:
        break
    d_obj_file.write(date)
s_obj_file.close()
d_obj_file.close()