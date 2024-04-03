#!/bin/bash

# Apt Settings
apt -y update
apt -y  upgrade
apt-get -y update
apt-get -y upgrade

# Install MongoDB
apt install -y curl
curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
apt-get install -y nodejs

# Install MongoDB Node.js Driver
npm i mongodb

# Entry Point
chmod +x ./entrypoint.sh
./entrypoint.sh