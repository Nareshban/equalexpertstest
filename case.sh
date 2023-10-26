#!/bin/bash

help(){
  if [ $1 == 'start' ] || [ $1 == 'test' ]
  then
          echo "Usage : $0 with start or test"
          exit
  fi
}

case "$1" in

start)  echo "Starting app"
    python getgistflask.py
    ;;
test)  echo  "Sending SIGINT signal"
    python getgistflask.py &
    pytest .
    ;;
   *)   help
     ;;
esac