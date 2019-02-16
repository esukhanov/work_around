#!/usr/bin/python
#  -*- coding: utf-8 -*-
import docker



image_name='mysql_ok'
mysql_pass='123456'
client = docker.from_env()
alpine_name='ubuntu_test'


def network():
    ipam_pool = docker.types.IPAMPool(
        subnet='124.42.0.0/16',
        iprange='124.42.0.0/24',
        gateway='124.42.0.254',
        aux_addresses={
            'reserved1': '124.42.1.1',
            'reserved2': '124.42.1.2'
        }
    )
    ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])
    return client.networks.create("network1", driver="bridge",ipam = ipam_config)

def network2():
    ipam_pool = docker.types.IPAMPool(
        subnet='114.42.0.0/16',
        iprange='114.42.0.0/24',
        gateway='114.42.0.254',
        aux_addresses={
            'reserved1': '114.42.1.1',
            'reserved2': '114.42.1.2'
        }
    )
    ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])
    return client.networks.create("network2", driver="bridge",ipam = ipam_config)

def mysql():
    #image =client.images.pull(image_name+':latest')
    image = client.images.list(name=image_name + ':latest')
    container=client.containers.run(image_name,
                                        detach=True,
                                        network="network1",
                                        links={'container': 'alias'},
                                        ports={'3306/tcp':'3306'},
                                        environment={'MYSQL_ROOT_PASSWORD':'password',
                                                    'MYSQL_DATABASE':'Test',
                                                    'default-authentication-plugin':'mysql_native_password'
                                                    })
    #net.connect(container)
    print (container.status)
    #print (net.containers)
    print (container.status)


def mysql2():
    #image =client.images.pull(image_name+':latest')
    image = client.images.list(name=image_name + ':latest')
    container=client.containers.run(image_name,
                                        detach=True,
                                        links={'container': 'alias'},
                                        network = "network2",
                                        ports={'3305/tcp':'3305'},
                                        environment={'MYSQL_ROOT_PASSWORD':'password',
                                                    'MYSQL_DATABASE':'Test',
                                                    'default-authentication-plugin':'mysql_native_password'
                                                    })
    #net.connect(container)
    print (container.status)
    #print (net.containers)
    print (container.status)
def alpine(net):
    #image =client.images.pull(image_name+':latest')
    image = client.images.list(name=alpine_name + ':latest')
    container=client.containers.run(alpine_name,
                                    tty=True,
                                    detach=True,
                                    ports={'8080/tcp':'8080'}
                                    )

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

remove_all_container_networks()
net=network()
net2=network2()
mysql()
mysql2()
#alpine(net2)
client.networks.prune()



# ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root'; FLUSH;
# GRANT ALL PRIVILEGES ON *.* TO root@'%' IDENTIFIED BY 'root'
# docker restart mysql

# docker run --name mysql -e MYSQL_ROOT_PASSWORD=password -d mysql:latest --default-authentication-plugin=mysql_native_password --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

#CREATE USER 'root'@'172.17.0.1'  IDENTIFIED BY 'password';
#GRANT ALL PRIVILEGES ON * . * TO 'root'@'172.17.0.1';
#FLUSH PRIVILEGES;

#docker exec -it mysql bash

#docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest
#docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:latest