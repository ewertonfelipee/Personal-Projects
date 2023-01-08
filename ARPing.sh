#!/bin/bash

if [ "$1" == "" ]
then
    echo "ARPing Sweep - EWERTON FELIPE"
    echo "Necessary root mode"
    echo "Usage: $0 NETWORK INTERFACE"
    echo "Example: $0 127.0.0.1 lo"
    
else
for host in $(seq 1 255);
do

var=$(arping -c 1 -w1 -i $2 $1.$host | grep "60 bytes" | cut -d " " -f5 | sed 's/)://' | sed 's/(//')
if [ "$var" != "" ]
then
echo "Active IP:$var"
else
continue
fi

done

fi
