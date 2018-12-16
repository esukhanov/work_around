#!/bin/bash
yum clean all
yum install epel-release
yum -y update
yum install git