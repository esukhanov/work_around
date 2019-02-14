#!/usr/bin/python
#  -*- coding: utf-8 -*-
import docker



#docker exec -it mysql bash

#docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest
#docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:latest
image_name='mysql_ok'
mysql_pass='123456'
client = docker.from_env()


def network():
    return client.networks.create("network1", driver="bridge")

def mysql(net):
    #image =client.images.pull(image_name+':latest')
    image = client.images.list(name=image_name + ':latest')
    container=client.containers.run(image_name,
                                       detach=True,
                                       ports={'3306/tcp':'3306'},
                                       environment={'MYSQL_ROOT_PASSWORD':'password',
                                                    'MYSQL_DATABASE':'Test',
                                                    'default-authentication-plugin':'mysql_native_password'
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
# ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root'; FLUSH;
# GRANT ALL PRIVILEGES ON *.* TO root@'%' IDENTIFIED BY 'root'
# docker restart mysql

# docker run --name mysql -e MYSQL_ROOT_PASSWORD=password -d mysql:latest --default-authentication-plugin=mysql_native_password --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

#CREATE USER 'root'@'172.17.0.1'  IDENTIFIED BY 'password';
#GRANT ALL PRIVILEGES ON * . * TO 'root'@'172.17.0.1';
#FLUSH PRIVILEGES;
remove_all_container_networks()
net=network()
mysql(net)
client.networks.prune()