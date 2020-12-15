#!/bin/bash

DIR="/home/mriantf/script_skripsi"
WORKDIR="${DIR}/script"

echo "Process sent email to ${1} ...."

/usr/local/bin/python3.8 ${WORKDIR}/create_pdf.py $1 $2 $3