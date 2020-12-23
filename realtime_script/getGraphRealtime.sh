#!/bin/bash

DIR="/home/mriantf/script_skripsi"
WORKDIR="${DIR}/REALTIME"
OUTPUT="${WORKDIR}/OUTPUT"
RRALOC="/var/lib/cacti/rra"
DTL="${WORKDIR}/data_list"
RTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

ls ${DTL} > ${WORKDIR}/tmp_list

if test -f `cat ${WORKDIR}/tmp_list`
then
	echo "ada" > ada
	for i in `cat ${WORKDIR}/tmp_list`
	do
		paramuniqID=`echo ${i} | awk -F'_' '{print $1}'`
		cat ${DTL}/${i} | grep ${paramuniqID} | while read line
		do
		uniqeID=`echo $line | awk -F';' '{print $1}'`
		report_title=`echo $line | awk -F';' '{print $2}'`
		startdate=`echo $line | awk -F';' '{print $3}'`
		enddate=`echo $line | awk -F';' '{print $4}'`
		email=`echo $line | awk -F';' '{print $5}'`
		periodic=`echo $line | awk -F';' '{print $6}'`
		rrd_file=`echo $line | awk -F';' '{print $7}'`
		rrd_name=`echo $line | awk -F';' '{print $8}'`
		filename=`echo $line | awk -F';' '{print $8}' | sed 's/ /_/g' | sed 's/\//-/g'`
		
		startdatesec=`date -d "${startdate}" +%s`
		enddatesec=`date -d "${enddate}" +%s`

		if [[ ${periodic} == "Days" ]]
		then
			for((z=${startdatesec}; z<${enddatesec}; z+=86400))
			do
				FN=`date -d @${z} '+%Y%m%d'`
				tglstart=`date -d @${z} '+%Y/%m/%d %H\:%M\:%S'`
				j=''
				if [[ $j > $enddatesec ]]
				then
				j=$(($enddatesec))
				else
				j=$(($z+86400))
				fi
				tglend=`date -d @${j} '+%Y/%m/%d %H\:%M\:%S'`

				/usr/bin/rrdtool graph ${OUTPUT}/${uniqeID}_${FN}_per${periodic}_${filename}.png \
				--imgformat=PNG \
				--start="${z}" \
				--end="${j}" \
				--pango-markup  \
				--title="${rrd_name}" \
				--vertical-label='bits/sec' \
				--slope-mode \
				--base=1000 \
				--height=120 \
				--width=500 \
				--rigid \
				--alt-autoscale-max \
				--lower-limit='0' \
				COMMENT:"From ${tglstart} To ${tglend}\c" \
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
				DEF:a="${RRALOC}/${rrd_file}":'traffic_in':MAX \
				DEF:b="${RRALOC}/${rrd_file}":'traffic_in':AVERAGE \
				DEF:c="${RRALOC}/${rrd_file}":'traffic_out':AVERAGE \
				DEF:d="${RRALOC}/${rrd_file}":'traffic_out':MAX \
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
			elif [[ $PERIODIC == "Weeks" ]]
		then
			for((z=${startdatesec}; z<${enddatesec}; z+=604800))
			do
				FN=`date -d @${z} '+%Y%m%d'`
				tglstart=`date -d @${z} '+%Y/%m/%d %H\:%M\:%S'`
				j=$(($z+518400))
				tglend=`date -d @${j} '+%Y/%m/%d %H\:%M\:%S'`

				/usr/bin/rrdtool graph ${OUTPUT}/${uniqeID}_${FN}_per${periodic}_${filename}.png \
				--imgformat=PNG \
				--start="${z}" \
				--end="${j}" \
				--pango-markup  \
				--title="${rrd_name}" \
				--vertical-label='bits/sec' \
				--slope-mode \
				--base=1000 \
				--height=120 \
				--width=500 \
				--rigid \
				--alt-autoscale-max \
				--lower-limit='0' \
				COMMENT:"From ${tglstart} To ${tglend}\c" \
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
				DEF:a="${RRALOC}/${rrd_file}":'traffic_in':MAX \
				DEF:b="${RRALOC}/${rrd_file}":'traffic_in':AVERAGE \
				DEF:c="${RRALOC}/${rrd_file}":'traffic_out':AVERAGE \
				DEF:d="${RRALOC}/${rrd_file}":'traffic_out':MAX \
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
			for((z=${startdatesec}; z<${enddatesec}; z+=2678400))
			do
				FN=`date -d @${z} '+%Y%m%d'`
				tglstart=`date -d @${z} '+%Y/%m/%d %H\:%M\:%S'`
				j=$(($z+2592000))
				tglend=`date -d @${j} '+%Y/%m/%d %H\:%M\:%S'`

				/usr/bin/rrdtool graph ${OUTPUT}/${uniqeID}_${FN}_per${periodic}_${filename}.png \
				--imgformat=PNG \
				--start="${z}" \
				--end="${j}" \
				--pango-markup  \
				--title="${rrd_name}" \
				--vertical-label='bits/sec' \
				--slope-mode \
				--base=1000 \
				--height=120 \
				--width=500 \
				--rigid \
				--alt-autoscale-max \
				--lower-limit='0' \
				COMMENT:"From ${tglstart} To ${tglend}\c" \
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
				DEF:a="${RRALOC}/${rrd_file}":'traffic_in':MAX \
				DEF:b="${RRALOC}/${rrd_file}":'traffic_in':AVERAGE \
				DEF:c="${RRALOC}/${rrd_file}":'traffic_out':AVERAGE \
				DEF:d="${RRALOC}/${rrd_file}":'traffic_out':MAX \
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
		fi
		done < ${DTL}/${i}
		/usr/local/bin/python3.8 ${RTDIR}/realtime_pdf.py $paramuniqID
	done
else
  echo "gak ada" > gaada
  exit
fi

rm -rf ${WORKDIR}/tmp_list
