#!/bin/bash
# info from
#https://docs.docker.com/install/linux/docker-ce/centos/#set-up-the-repository

sudo yum install -y yum-utils \
device-mapper-persistent-data \
lvm2

sudo yum-config-manager \
--add-repo \
https://download.docker.com/linux/centos/docker-ce.repo

sudo yum install docker-ce

sudo systemctl start docker

sudo docker run hello-world