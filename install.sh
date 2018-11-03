#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   printf "ERROR: This script must be run as root (sudo)!\n"
   exit 1
fi

pip install requests
pip install netaddr
