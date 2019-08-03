#!/usr/bin/env bash


#https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198

docker pull postgres
mkdir -p $HOME/docker/volumes/postgres
docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres