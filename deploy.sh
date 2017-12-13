#!/bin/bash
apt update
export DEBIAN_FRONTEND=noninteractive
apt upgrade -y
apt install python-pip -y
apt install git -y
apt install virtualenv -y
pip install fabric 
adduser --disabled-password --gecos "" django
echo -e "password4455\npassword4455\n" | sudo passwd django
wget https://raw.githubusercontent.com/smokeme/states/master/fabfile.py
fab deploy
