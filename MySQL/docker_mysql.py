#!/usr/bin/python
#  -*- coding: utf-8 -*-
import docker



#docker exec -it mysql bash

#docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest
#docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:latest
image_name='mysql'
mysql_pass='123456'
client = docker.from_env()


def network():
    return client.networks.create("network1", driver="bridge")

def mysql(net):
    image =client.images.pull(image_name+':latest')
    container=client.containers.run(image_name,
                                       detach=True,
                                       ports={'3306/tcp':'3306'},
                                       environment={'MYSQL_ROOT_PASSWORD':'password'
                                                    })
    net.connect(container)
    print (container.status)
    print (net.containers)
    print (container.status)

def remove_all_container_networks():
    for container in client.containers.list(all=True):
        container.remove(force=True)
    #remove unused
    client.networks.prune()
    # try remove
    #for inet in client.networks.list():
    #    if inet.name not in ('none','host','bridge'):
    #        inet.remove()
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
remove_all_container_networks()
net=network()
mysql(net)
client.networks.prune()