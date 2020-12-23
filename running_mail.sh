#!/bin/bash

# DIR="/home/mriantf/script_skripsi"
# WORKDIR="${DIR}/script"

WORKDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Process sent email to ${1} ...."

/usr/local/bin/python3.8 ${WORKDIR}/sent_mail.py $1 $2 $3
