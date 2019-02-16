#!/usr/bin/python
#  -*- coding: utf-8 -*-
import docker
import os
image_name='ubuntu_test'
client = docker.from_env()
print (os.getcwd())

def create_image():
    i_n='ubuntu'
    # docker build . -t ubuntu_test:latest
    #image = client.images.pull(i_n+':latest')
    image=client.images.build(path =os.getcwd(),tag=image_name)
    print (image)

def network():
    ipam_pool = docker.types.IPAMPool(
        subnet='104.42.0.0/16',
        iprange='104.42.0.0/24',
        gateway='104.42.0.254',
        aux_addresses={
            'reserved1': '104.42.1.1'        }
    )
    ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])
    return client.networks.create("network1", driver="bridge",ipam = ipam_config)
def ubuntu(net):
    #image =client.images.pull(image_name+':latest')
    image = client.images.list(name=image_name + ':latest')
    container=client.containers.run(image_name,
                                       detach=True
                                    )
    net.connect(container)
    print (container.status)
    print (net.containers)
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
#create_image()
#net=network()
#ubuntu(net)