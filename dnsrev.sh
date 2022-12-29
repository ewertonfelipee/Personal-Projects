#!/bin/bash


# Válido para esse host
# Para outros hosts alterar o bloco for do script

if [ "$1" == "" ]
then
 echo "DNS Reverse - EWERTON FELIPE"
 echo "Usage: ./dnsrev businesscorp.com.br"
 
else
  ip=$(host $1 | cut -d " " -f4 | grep -v "handled")
  echo "O bloco de rede eh: "
  whois $ip | grep "inetnum" | cut -d ":" -f2 | sed 's/        //'
  
  for dns in $(seq 224 239)
  do
  host -t ptr 37.59.174.$dns | grep -v "37.59.174" | cut -d " " -f5
  done

fi
