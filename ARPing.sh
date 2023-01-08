#!/bin/bash

if [ "$1" == "" ]
then
    echo "ARPing Sweep"
    echo "Usage: $0 NETWORK interface"
    echo "Example: $0 192.168.0 eth0"
    echo "Uses in root mode"
else
for host in {1..254};
do
arping -c 1 -i $2 $1.$host | grep "60 bytes"
done

fi
