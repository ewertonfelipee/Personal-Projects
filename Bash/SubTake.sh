#!/bin/bash

if [ "$1" == "" ]
then
	echo "Subdomain Takeover Script by Ewerton Felipe"
	echo "Usage: ./subtake domain"

else
 for sub in $(cat lista)
 do
		host -t cname $sub.$1 | egrep -v "NXDOMAIN|CNAME record"
 done
fi
