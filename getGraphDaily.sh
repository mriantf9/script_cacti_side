#!/bin/bash


##DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


DIR="/home/mriantf/script_skripsi"
DT_RP="${DIR}/DATA_REPORT/Monthly"
WORKDIR="${DIR}/script"

ls ${DT_RP}/ > ${WORKDIR}/tmp_list


for j in `cat ${WORKDIR}/tmp_list`
  do
    cat ${DT_RP}/${j} | while read line
	do
	  REPORT_ID=`echo $line | awk -F';' '{print $1}'`
	  REPORT_NAME=`echo $line | awk -F';' '{print $4}'`
	  GTYPE=`echo $line | awk -F';' '{print $5}'`
	  RRDFILE=`echo $line | awk -F';' '{print $6}'`
	  RRDNAME=`echo $line | awk -F';' '{print $7}'`
	  FILENAME=`echo $line | awk -F';' '{print $7}' | sed 's/ /_/g' | sed 's/\//-/g'`
	  PERIODIC=`echo $line | awk -F';' '{print $8}'`
	  
	  if [ $PERIODIC == "Days" ]
	  then
	    /usr/bin/bash ${WORKDIR}/periodicGraph/graphPerDays.sh $REPORT_ID $GTYPE $FILENAME $RRDNAME $RRDFILE
	  elif [ $PERIODIC == "Weeks" ]
	  then
		/usr/bin/bash ${WORKDIR}/periodicGraph/graphPerWeeks.sh $REPORT_ID $GTYPE $FILENAME $RRDNAME $RRDFILE
	  else
	    /usr/bin/bash ${WORKDIR}/periodicGraph/graphPerMonth.sh $REPORT_ID $GTYPE $FILENAME $RRDNAME $RRDFILE
	  fi
	  
	done < ${DT_RP}/${j}
done
rm -rf ${WORKDIR}/tmp_list

