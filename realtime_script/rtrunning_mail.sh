#!/bin/bash

my_touch() {
 if test -f $1
 then
  rm -f $1
  touch $1
 else
  touch $1
 fi
}

user=`whoami`
DIR="/home/${user}/script_skripsi"
logrt="${DIR}/REALTIME/log"
WORKDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dt=`date '+%Y%m%d'`
echo "Process sent email to ${1} ...."

my_touch ${logrt}/${dt}_$3_$2.log
/usr/local/bin/python3.8 ${WORKDIR}/rtsent_mail.py $1 $2 $3 >> ${logrt}/${dt}_$3_$2.log
