import asyncio
import time

class Manager():

    names = []

    def prepare_message(self,message):
        print(f'prepare_message {message}')
        if 'name' in message:
            name = message.split(' ')[1]
            if name in Manager.names:
                return 'User have allready registered'.encode()
            else:
                Manager.names.append(name)
                return f'New user {name} registered'.encode()

        else:
            print('easy message')
            return message.encode()


class Server(Manager):

    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

    async def handle_echo(self,reader, writer):
        while True:
            print('wait message')
            data = await reader.read(512)

            print("Received %r from %r" % (data.decode(), writer.get_extra_info('peername')))


            request = self.prepare_message(data.decode())
            print("Send: %r" % request.decode())
            writer.write(request)
            await writer.drain()

            #print("Close the client socket")
            #writer.close()


    def start(self):
        self.loop = asyncio.get_event_loop()
        coro = asyncio.start_server(self.handle_echo, self.ip, self.port, loop=self.loop)
        self.server = self.loop.run_until_complete(coro)
        self.loop.run_forever()

    def stop(self):
        self.server.close()
        self.loop.run_until_complete(server.wait_closed())
        self.loop.close()



if __name__ == '__main__':

    server = Server('127.0.0.1',8888).start()
