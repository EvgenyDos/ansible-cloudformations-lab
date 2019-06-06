#!/bin/bash

if [ -z "$1" ]; then
  echo "Hello world"
  exit 0
fi

case "$1" in
  centos) 
    echo "CentOS system"
    ;;
  *)      
    echo "Not a CentOS system"
    ;;
esac

