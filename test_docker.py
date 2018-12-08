#!/usr/bin/python
#  -*- coding: utf-8 -*-
from io import BytesIO
from docker import DockerClient

import docker
client = docker.from_env()
print client