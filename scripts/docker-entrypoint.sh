#!/bin/sh

cd /code/iota_api/

if $ENABLE_BATCHING;then
  sed -i "5s/False/True/g" conf  
fi
if true
then
  sed -i "2s/localhost/${HOST_IP}/g" conf
fi

python app.py
