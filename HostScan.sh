#!/bin/bash

echo "Malware Analysis"
echo "==========================="
for host in $(seq 1 254);
do
hping3 -c 1 -p 13 -S 172.16.1.$host 2> /dev/null;
hping3 -c 1 -p 37 -S 172.16.1.$host 2> /dev/null;
hping3 -c 1 -p 30000 -S 172.16.1.$host 2> /dev/null;
hping3 -c 1 -p 3000 -S 172.16.1.$host 2> /dev/null;
hping3 -c 1 -p 1337 -S 172.16.1.$host 2> /dev/null | grep "flags=SA";
echo "==========================="
done
