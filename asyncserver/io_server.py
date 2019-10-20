#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import asyncio

class Data_machine():

    DATA = {}

    def __init__(self,addr = 0,data = 0):
        print('init')
        if Data_machine.DATA.get(addr):
            old_rec = Data_machine.DATA[addr]
            old_rec.append(data)
            Data_machine.DATA[addr] = old_rec
        else:
            Data_machine.DATA[addr] = [data]

    def show_data(self):
        print('****************')
        for rec in Data_machine.DATA:
            print(rec)
            print(Data_machine.DATA[rec])
        print('****************')


async def server(reader,writer):

    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))
    addr = f'{addr[0]}:{addr[1]}'
    dm = Data_machine(addr = addr,data = message)
    dm.show_data()
    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()

    print("Close the client socket")
    writer.close()



loop = asyncio.get_event_loop()
coro = asyncio.start_server(server, '192.168.31.13', 8888, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass