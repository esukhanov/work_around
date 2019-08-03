#!/usr/bin/python
#  -*- coding: utf-8 -*-
import asyncio
import time
import random
import  concurrent.futures
import glob,os

class Textwriter():

    path_to_file = r'C:\Users\BD\PycharmProjects\untitled2\async_try_write_file\files\\'


    def __init__(self,filename,message):
        self.message= message + '\n'
        self.file_name = filename
        self.buffer= ''

    def syncwrt(self):
        for i in range(2000):

            with open(self.path_to_file + self.file_name+str(i), 'a') as file:
                file.write(self.message)

    def wrtblocking(self,ind):
        with open(self.path_to_file + self.file_name + str(ind), 'a') as file:
            file.write(self.message)

    async def asyncwrt(self,executor):

        loop = asyncio.get_event_loop()
        blocking_tasks = [
            loop.run_in_executor(executor, self.wrtblocking, i)
            for i in range(2000)
        ]
        completed, pending = await asyncio.wait(blocking_tasks)



    def remove_files(self):
        files = glob.glob(self.path_to_file[:-1]+'*')
        for f in files:
            #print(f)
            os.remove(f)


b=Textwriter('text1.txt','#asdfsadfadsfsadfsdafasdfasdf#')
executor = concurrent.futures.ThreadPoolExecutor(max_workers=50)
event_loop = asyncio.get_event_loop()
try:
    a = time.time()
    event_loop.run_until_complete(
        b.asyncwrt(executor)
    )
finally:
    print(time.time() - a)
    event_loop.close()

time.sleep(2)
b.remove_files()



b=Textwriter('text.txt','#asdfsadfadsfsadfsdafasdfasdf#')
a = time.time()
b.syncwrt()
print(time.time() - a)
time.sleep(2)
b.remove_files()