#!/bin/bash

if [ "$1" == "postinst" ]; then
  mv actions{,.tmp}.py
  mv actions{.postinst,}.py
fi

sudo eopkg bi --ignore-safety pspec.xml
