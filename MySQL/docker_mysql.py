#!/usr/bin/python
#  -*- coding: utf-8 -*-
import docker


image_name='mysql'
mysql_pass='123456'
client = docker.from_env()
image =client.images.pull(image_name+':latest')
container=client.containers.create(image_name, detach=True)
client.containers.run(image_name,command='run --name some-mysql -e MYSQL_ROOT_PASSWORD='+mysql_pass+' -d '+ image_name+':latest')
print (container.status)