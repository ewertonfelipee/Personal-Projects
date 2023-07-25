#!/bin/bash

if [ "$1" == "" ]
then
	echo "Parsing Html"
	echo "Example: $0 google.com.br"

else
grep href index.html | cut -d "/"  -f 3 | grep "\." | cut -d '"' -f 1 | grep -v "<l" > lista
for list in $(cat lista)
do
host $list | sed '/not found/d';
done

fi
