#!/usr/bin/python
#  -*- coding: utf-8 -*-
from io import BytesIO
from docker import DockerClient

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
            self.client.containers.remove()

    def start_image(self):
        self.container = self.client.containers.run(self.image_name, detach=True)


docker=Docker_Handler(centos7_image_name)
docker.start_image()
docker.remove_all_images()