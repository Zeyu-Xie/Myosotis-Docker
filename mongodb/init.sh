#!/bin/bash

apt -y update
apt -y  upgrade
apt-get -y update
apt-get -y upgrade

apt install -y curl

curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
apt-get install -y nodejs