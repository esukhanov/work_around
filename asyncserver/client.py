#!/usr/bin/env python3
import socket
import time
import random
from threading import Thread

class Clients():
    def __init__(self,number):
        self.number_of_clients=number

    def start(self):

        for _cient_num in range(self.number_of_clients):
            client_tread=Thread(target=self.client,args=(_cient_num,))
            client_tread.start()

    def client(self,_cient_num):
        name=random.choice('afdgjklouytrew')+random.choice('afdgjklouytrew')+random.choice('afdgjklouytrew')+str(_cient_num)
        delay = random.randint(0,3)
        bind_ip = '192.168.31.13'
        bind_port = 8888
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((bind_ip, bind_port))
        #time.sleep(delay)
        #client.send('sadfasdf'.encode())
        #response = client.recv(4096)
        #print('get %s '%response)

        #while True:
        time.sleep(delay)
        client.send('sadfasdf'.encode())
        
            #mesage=input('Enter your message:')
            #mesage='ping from '+ name
            #client.send(mesage.encode())
            #response = client.recv(4096)
            #print('get %s '%response)

            #time.sleep(0.1)

cl=Clients(100)
cl.start()