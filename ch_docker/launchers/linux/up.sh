#!/bin/bash

# linux ch01 docker startup script.
# author: liebl@informatik.uni-leipzig.de

cd "$(dirname "$0")/../../docker"
export USER_HOME="${HOME}"
export USER_ID="${UID}"

# run Jupyter with the same user id so we can read and write $USER_HOME. we
# specify --build in case this gets run for various users. 
sudo HOME="${USER_HOME}" JUPYTER_USER="${USER_ID}" docker-compose up --build
