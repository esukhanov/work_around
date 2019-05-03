#!/usr/bin/env python3
import socket
import threading
bind_ip = '192.168.31.13'
bind_port = 8082


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

def handle_client_connection(client_socket):
    while True:
        request = client_socket.recv(1024)
        print ('Received %s'%(request))
        client_socket.send('ACK!'.encode())
        #client_socket.close()

while True:
    client_sock, address = server.accept()

    client_handler = threading.Thread(target= handle_client_connection, args=(client_sock,))
    client_handler.start()