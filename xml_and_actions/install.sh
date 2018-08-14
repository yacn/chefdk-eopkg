#!/bin/bash

if [ ! -f "chefdk*.eopkg" ]; then
  ./build.sh $@
fi

sudo eopkg it chefdk-*.eopkg

if [ "$1" == "postinst" ]; then
  mv actions{,.postinst}.py
  mv actions{.tmp,}.py
fi
