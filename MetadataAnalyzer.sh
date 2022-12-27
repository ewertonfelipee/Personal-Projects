#!/bin/bash

if [ "$1" == "" ]
then
    echo "MetaData Analyzer - EWERTON FELIPE"
    echo "Usage: ./metadataanalyzer target filetype"
  
else
  lynx --dump "www.google.com/search?&q=site:$1+filetype:$2" | grep ".$2" | cut -d "=" -f 2 | egrep -v "site|google" | sed 's/...$//' > metadata
  
  for url in $(cat metadata)
  do
    echo "==========MetaData=========="
    wget $url
    exiftool *.$2;
  done
fi
