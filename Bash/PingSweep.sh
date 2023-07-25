#!/bin/bash

if [ "$1" == "" ]
then
    echo "Ping Sweep"
    echo "Usage: $0 NETWORK"
    echo "Example: $0 127.0.0.1"
else
for host in {1..254};
do
ping -c 1 $1.$host | grep "64 bytes" | cut -d ":" -f 1 | cut -d " " -f 4;
done

fi
