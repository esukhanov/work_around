#!/usr/bin/python
#  -*- coding: utf-8 -*-
from io import BytesIO
from docker import DockerClient
import time
import docker
centos7_image_name='centos'


class Docker_Handler():
    def __init__(self,image_name):
        self.image_name=image_name
        self.client=docker.from_env()
        self.container=None
        self.image=None
        self.pull_image()

    def pull_image(self):
        self.image =self.client.images.pull(centos7_image_name+':latest')

    def remove_all_images(self):
        for image in self.client.images.list():
            print image
            print dir(image)
            self.client.images.remove(image.id,force=True)

    def remove_all_containers(self):
        for container in self.client.containers.list(all=True):
            print container
            print dir(container)
            container.remove(force=True)

    def create_container(self):
        self.container = self.client.containers.create(self.image_name, detach=True)


docker=Docker_Handler(centos7_image_name)
docker.create_container()

docker.container.start()
time.sleep(2)
print docker.container.status
time.sleep(2)
docker.container.stop()
docker.remove_all_containers()
docker.remove_all_images()