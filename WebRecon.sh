#!/bin/bash

for i in $(cat wordlist)
do
var=$(curl -s -H "User-Agent: toolTon" -o /dev/null -w "%{http_code}" $1/$i.$2)
if [ $var == "200" ]
then 
echo "Diretorio encontrado: $1/$i.$2";
fi
done
