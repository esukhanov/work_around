#!/usr/bin/python
#  -*- coding: utf-8 -*-

class Common():

    instance = None

class Singletone(Common):

    print (Common.instance)

    class __Singletone(Common,object):

        def __init__(self):
            print('init')


        def __getattr__(self, name):
            print('__getattr__')
            return getattr(Common.instance, name)

        def __setattr__(self, name,value):
            print('set')
            Common.instance.__dict__[name]=value


    def __new__(cls,*args,**kwargs): # __new__ always a classmethod
        print ('new')

        if not Common.instance:
            Common.instance = Singletone.__Singletone(*args,**kwargs)
        return Common.instance




class MainClass(Singletone):

    def init(self,a,b,c):
        Singletone.__init__(self)
        self.a=a
        self.b=b
        self.c=c

    def __new__(cls,*args,**kwargs):
        return super(MainClass, cls).__new__(cls)

a=MainClass(1,2,3)

print(a)
a.val=12
a.a=123
print(a.val)
print(a.a)
print ('*******************')
#print(id(a))
b=MainClass(1,2,3,4,5,6)
#print(id(b))
print (b.val)
print(b.a)









