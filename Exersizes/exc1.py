#!/usr/bin/python
#  -*- coding: utf-8 -*-
import os
name='test'
#print (os.path.dirname(__file__))
#print (os.path.join(os.path.dirname(__file__+'/')))
a=set([4,4,2,2,2,2,1,1,1,1,3,3,3,2,5,1])
import time
def a(n):
    return lambda a:a*n



class A():
    DATA = {}
    def __init__(self,data = 0,data2 = 0):
        print('init')
        if A.DATA.get(data):
            old_rec = A.DATA[data]
            old_rec.append(data2)
            A.DATA[data] = old_rec
        else:
            A.DATA[data] = [data2]

a= A(data = 'asd',data2 = 122)
a= A(data = 'asds',data2 = 1222)
a= A(data = 'asds',data2 = 1222)

print(A.DATA)