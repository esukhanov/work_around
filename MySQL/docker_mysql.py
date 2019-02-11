#!/usr/bin/python
#  -*- coding: utf-8 -*-
import docker


image_name='mysql'

client = docker.from_env()
image =client.images.pull(image_name+':latest')
container=client.containers.create(image_name, detach=True)
client.containers.run(image_name)
print (container.status)