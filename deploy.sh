#!/bin/bash
apt update
apt upgrade -y
apt install python-pip -y
apt install git -y
apt install virtualenv -y
pip install fabric 
adduser --disabled-password --gecos "" django
echo -e "password4455\npassword4455\n" | sudo passwd django
wget https://raw.githubusercontent.com/mhadam/testing-goat/master/deploy_tools/fabfile.py 
fab deploy
