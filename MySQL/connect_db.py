#!/usr/bin/python
#  -*- coding: utf-8 -*-
import pymysql.cursors

# Подключиться к базе данных.
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='password',
                             db='Ass',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             )