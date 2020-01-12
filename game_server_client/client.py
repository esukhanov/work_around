import socket
import time
from itertools import cycle
import threading

class Client(threading.Thread):

    BUFFER_SIZE = 1024

    def __init__(self,ip , port, name):
        super(Client, self).__init__()
        self.ip = ip
        self.port = port
        self.name = name
        self.message = cycle([f'name {self.name}','hello','bye'])




    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))
        print('connect')

    def read_data(self):
        print('wait data')
        data = self.s.recv(Client.BUFFER_SIZE).decode()
        print(f'read data {data}')
        return data

    def send_data(self,message):
        print(f'send message {message}')
        message = message.encode()
        res = self.s.send(message)
        print(f'send res {res}')


    def run(self):
        self.connect()
        while True:
            self.send_data(next(self.message))
            data = self.read_data()
            time.sleep(2)

if __name__ == '__main__':

    ip = '127.0.0.1'
    port = 8888
    name = 'Test'
    names = ['Vasya','Sergey','Evgenii']
    # client = Client(ip,port,name)
    # client.start()
    for name in names:
        client = Client(ip, port, name)
        client.start()