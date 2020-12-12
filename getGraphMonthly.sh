#!/bin/bash


##DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


DIR="/home/mriantf/script_skripsi"
DT_RP="${DIR}/DATA_REPORT/Monthly"
WORKDIR="${DIR}/script"
OUTPUT="${DIR}/OUTPUT"
RRALOC="/var/lib/cacti/rra"

###################################
###################################
######## FOR DAYS AND WEEKS #######
INTERVAL=`date -d 'now-31days' +%s`
NOW=`date -d now +%s`
##################################
##################################

FN=`date -d @${NOW} '+%Y%m%d'`

###################################
###################################
######## FOR MONTH ################
L_START=`date -d @${INTERVAL} '+%Y/%m/%d %H\:%M\:%S'`
L_END=`date -d @${NOW} '+%Y/%m/%d %H\:%M\:%S'`
##################################
##################################

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
	    for((i=$INTERVAL; i<$NOW; i+=86400))
		do
			FN=`date -d @${i} '+%Y%m%d'`
			START=`date -d @${i} '+%Y/%m/%d %H\:%M\:%S'`
			j=$(($i+86400))
			END=`date -d @${j} '+%Y/%m/%d %H\:%M\:%S'`

			/usr/bin/rrdtool graph ${OUTPUT}/${GTYPE}/${FN}_ReportID${REPORT_ID}_${GTYPE}_per${PERIODIC}_${FILENAME}.png \
			--imgformat=PNG \
			--start="${i}" \
			--end="${j}" \
			--pango-markup  \
			--title="${RRDNAME}" \
			--vertical-label='bits/sec' \
			--slope-mode \
			--base=1000 \
			--height=120 \
			--width=500 \
			--rigid \
			--alt-autoscale-max \
			--lower-limit='0' \
			COMMENT:"From ${START} To ${END}\c" \
			COMMENT:"  \n" \
			--color BACK#F3F3F3 \
			--color CANVAS#FDFDFD \
			--color SHADEA#CBCBCB \
			--color SHADEB#999999 \
			--color FONT#000000 \
			--color AXIS#2C4D43 \
			--color ARROW#2C4D43 \
			--color FRAME#2C4D43 \
			--border 1 --font TITLE:11:'Arial' \
			--font AXIS:8:'Arial' \
			--font LEGEND:8:'Courier' \
			--font UNIT:8:'Arial' \
			--font WATERMARK:6:'Arial' \
			--slope-mode \
			--watermark 'Generated by Cacti®' \
			DEF:a="${RRALOC}/${RRDFILE}":'traffic_in':MAX \
			DEF:b="${RRALOC}/${RRDFILE}":'traffic_in':AVERAGE \
			DEF:c="${RRALOC}/${RRDFILE}":'traffic_out':AVERAGE \
			DEF:d="${RRALOC}/${RRDFILE}":'traffic_out':MAX \
			CDEF:cdefa='a,8,*' \
			CDEF:cdefb='b,8,*' \
			CDEF:cdeff='c,8,*' \
			CDEF:cdefg='d,8,*' \
			LINE1:cdefa#00CF00FF:  \
			AREA:cdefb#00CF00FF:'Inbound '  \
			GPRINT:cdefb:LAST:'Current\:%8.2lf%s'  \
			GPRINT:cdefb:AVERAGE:'Average\:%8.2lf%s'  \
			GPRINT:cdefb:MAX:'Maximum\:%8.2lf%s\n'  \
			LINE1:cdeff#002A97FF:'Outbound'  \
			LINE1:cdefg#002A97FF:  \
			GPRINT:cdefg:LAST:'Current\:%8.2lf%s'  \
			GPRINT:cdefg:AVERAGE:'Average\:%8.2lf%s'  \
			GPRINT:cdefg:MAX:'Maximum\:%8.2lf%s' 
		done
	  elif [ $PERIODIC == "Weeks" ]
	  then
		for((i=$INTERVAL; i<$NOW; i+=604800))
		do
			FN=`date -d @${i} '+%Y%m%d'`
			START=`date -d @${i} '+%Y/%m/%d %H\:%M\:%S'`
			j=$(($i+518400))
			END=`date -d @${j} '+%Y/%m/%d %H\:%M\:%S'`

			/usr/bin/rrdtool graph ${OUTPUT}/${GTYPE}/${FN}_ReportID${REPORT_ID}_${GTYPE}_per${PERIODIC}_${FILENAME}.png \
			--imgformat=PNG \
			--start="${i}" \
			--end="${j}" \
			--pango-markup  \
			--title="${RRDNAME}" \
			--vertical-label='bits/sec' \
			--slope-mode \
			--base=1000 \
			--height=120 \
			--width=500 \
			--rigid \
			--alt-autoscale-max \
			--lower-limit='0' \
			COMMENT:"From ${START} To ${END}\c" \
			COMMENT:"  \n" \
			--color BACK#F3F3F3 \
			--color CANVAS#FDFDFD \
			--color SHADEA#CBCBCB \
			--color SHADEB#999999 \
			--color FONT#000000 \
			--color AXIS#2C4D43 \
			--color ARROW#2C4D43 \
			--color FRAME#2C4D43 \
			--border 1 --font TITLE:11:'Arial' \
			--font AXIS:8:'Arial' \
			--font LEGEND:8:'Courier' \
			--font UNIT:8:'Arial' \
			--font WATERMARK:6:'Arial' \
			--slope-mode \
			--watermark 'Generated by Cacti®' \
			DEF:a="${RRALOC}/${RRDFILE}":'traffic_in':MAX \
			DEF:b="${RRALOC}/${RRDFILE}":'traffic_in':AVERAGE \
			DEF:c="${RRALOC}/${RRDFILE}":'traffic_out':AVERAGE \
			DEF:d="${RRALOC}/${RRDFILE}":'traffic_out':MAX \
			CDEF:cdefa='a,8,*' \
			CDEF:cdefb='b,8,*' \
			CDEF:cdeff='c,8,*' \
			CDEF:cdefg='d,8,*' \
			LINE1:cdefa#00CF00FF:  \
			AREA:cdefb#00CF00FF:'Inbound '  \
			GPRINT:cdefb:LAST:'Current\:%8.2lf%s'  \
			GPRINT:cdefb:AVERAGE:'Average\:%8.2lf%s'  \
			GPRINT:cdefb:MAX:'Maximum\:%8.2lf%s\n'  \
			LINE1:cdeff#002A97FF:'Outbound'  \
			LINE1:cdefg#002A97FF:  \
			GPRINT:cdefg:LAST:'Current\:%8.2lf%s'  \
			GPRINT:cdefg:AVERAGE:'Average\:%8.2lf%s'  \
			GPRINT:cdefg:MAX:'Maximum\:%8.2lf%s' 
		done
	  else
	    /usr/bin/rrdtool graph ${OUTPUT}/${GTYPE}/${FN}_ReportID${REPORT_ID}_${GTYPE}_per${PERIODIC}_${FILENAME}.png \
		--imgformat=PNG \
		--start="${INTERVAL}" \
		--end="${NOW}" \
		--pango-markup  \
		--title="${RRDNAME}" \
		--vertical-label='bits/sec' \
		--slope-mode \
		--base=1000 \
		--height=120 \
		--width=500 \
		--rigid \
		--alt-autoscale-max \
		--lower-limit='0' \
		COMMENT:"From ${L_START} To ${L_END}\c" \
		COMMENT:"  \n" \
		--color BACK#F3F3F3 \
		--color CANVAS#FDFDFD \
		--color SHADEA#CBCBCB \
		--color SHADEB#999999 \
		--color FONT#000000 \
		--color AXIS#2C4D43 \
		--color ARROW#2C4D43 \
		--color FRAME#2C4D43 \
		--border 1 --font TITLE:11:'Arial' \
		--font AXIS:8:'Arial' \
		--font LEGEND:8:'Courier' \
		--font UNIT:8:'Arial' \
		--font WATERMARK:6:'Arial' \
		--slope-mode \
		--watermark 'Generated by Cacti®' \
		DEF:a="${RRALOC}/${RRDFILE}":'traffic_in':MAX \
		DEF:b="${RRALOC}/${RRDFILE}":'traffic_in':AVERAGE \
		DEF:c="${RRALOC}/${RRDFILE}":'traffic_out':AVERAGE \
		DEF:d="${RRALOC}/${RRDFILE}":'traffic_out':MAX \
		CDEF:cdefa='a,8,*' \
		CDEF:cdefb='b,8,*' \
		CDEF:cdeff='c,8,*' \
		CDEF:cdefg='d,8,*' \
		LINE1:cdefa#00CF00FF:  \
		AREA:cdefb#00CF00FF:'Inbound '  \
		GPRINT:cdefb:LAST:'Current\:%8.2lf%s'  \
		GPRINT:cdefb:AVERAGE:'Average\:%8.2lf%s'  \
		GPRINT:cdefb:MAX:'Maximum\:%8.2lf%s\n'  \
		LINE1:cdeff#002A97FF:'Outbound'  \
		LINE1:cdefg#002A97FF:  \
		GPRINT:cdefg:LAST:'Current\:%8.2lf%s'  \
		GPRINT:cdefg:AVERAGE:'Average\:%8.2lf%s'  \
		GPRINT:cdefg:MAX:'Maximum\:%8.2lf%s'
	  fi
	  
	done < ${DT_RP}/${j}
done
rm -rf ${WORKDIR}/tmp_list

/usr/local/bin/python3.8 ${WORKDIR}/create_pdf.py $GTYPE


