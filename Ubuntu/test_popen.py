#!/usr/bin/env python3
#  -*- coding: utf-8 -*-



import subprocess

cmd = 'telnet ya.ru'

p= subprocess.Popen(cmd,shell = True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

while p.poll():
    line = p.stdout.readline()
    if line:
        print(line)

