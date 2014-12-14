#!/bin/bash


sudo sh -c '

HOME_DIR=/home/pi
APPS_DIR=${HOME_DIR}/apps
LOGS_DIR=${APPS_DIR}/log

cd ${APPS_DIR}

. ./venv/bin/activate

./raspecitoWeb.py >${LOGS_DIR}/raspecitoWeb.log 2>&1 &'
