#!/bin/bash
apt update -y
apt install apache2 -y
apt install python3-pip -y
python3 -m pip install awscli