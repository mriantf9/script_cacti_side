#!/usr/bin/python3.8
from fpdf import FPDF
import os
from os import listdir
import sys
import csv
import subprocess
import fnmatch
from datetime import datetime, timedelta

##FOR FILTER##
import glob

##FOR SEPARATE##
import re


DIR="/home/mriantf/script_skripsi"
WORKDIR=DIR+"/REALTIME"
OUTPDF=WORKDIR+"/OUTPUT_PDF"
SRC_IMG=WORKDIR+"/OUTPUT"
filecsvnya = WORKDIR+"/data_list"
ARCHV = WORKDIR+"/ARCHIVE"
UNIQCODE = sys.argv[1]
csv_list = fnmatch.filter(os.listdir(WORKDIR+"/data_list"), UNIQCODE+"*.csv")
#csv_list = listdir(WORKDIR+"/data_list")

TITLE = ''
PERIODIC = ''
PDFNAME = ''

TODAY = datetime.now()
datefile = TODAY.strftime("%Y%b%d_%H%M%S")


######################################
########### LOOP FILE CSV ############
######################################
for filecsv in csv_list:
    pdf = FPDF('L','mm','Letter')

    ###################################
    ######### OPEN FILE CSV ###########
    ###################################
    with open (filecsvnya+'/'+filecsv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        #line_count = 0
        idx = 1

        ###############################
        ##### LOOP ROW CSV FILE #######
        ###############################
        for row in csv_reader:
           # print(row)
           # exit()
            TITLE = row[1]
            STARTDATE = row[2]
            ENDDATE = row[3]
            EMAIL = row[4]
            PERIODIC = row[5]
            PDFNAME = TITLE.replace(" ", "_")
            RRDTITLE = row[7]
            RRDTITLE2 = RRDTITLE.replace(" ", "_")
            RRDTITLE3 = RRDTITLE2.replace("/","-")

            filelist = fnmatch.filter(os.listdir(SRC_IMG+'/'), UNIQCODE+"*"+RRDTITLE3+".png")

            for imglist in filelist:
                path = SRC_IMG+'/'+imglist

                #################################
                ######### CREATE PDF ############
                #################################
                pdf.add_page()
                pdf.set_font("Times", size=15)
                pdf.cell(250, 20, txt=TITLE, ln=1, align="C")
                pdf.cell(250, 2, "From "+str(STARTDATE)+" - "+str(ENDDATE), ln=2, align="C")
                pdf.ln(3)
                pdf.cell(250, 10, txt="Periodic Graph Capture - per"+PERIODIC, ln=1, align="C")
                pdf.cell(0, 20, str(idx) + '. Traffic Pemakaian ' + RRDTITLE, 0, 1)
                pdf.ln(10)
                # print (imglist)
                pdf.image(path, 45, 65, 190, 80)
                idx += 1
        pdf.output(OUTPDF+'/'+UNIQCODE+"_"+PDFNAME+".pdf")

        #################################
        ######### SENT MAIL ############
        ################################
        PDFLIST = fnmatch.filter(os.listdir(OUTPDF+'/'), UNIQCODE+"*.pdf")
        print(PDFLIST)
        for PDFFILELIST in PDFLIST:
           os.system("/usr/bin/bash "+DIR+'/script/realtime_script/rtrunning_mail.sh ' +EMAIL+" "+PDFFILELIST+" "+UNIQCODE)
           print("Moving "+PDFFILELIST+" to archive")
           os.system("mv "+OUTPDF+'/'+PDFFILELIST+ " "+ARCHV+'/'+datefile+"_"+PDFFILELIST)
           
        print("Deleting data source "+filecsv+" ...")
        os.system("rm -rf "+filecsvnya+'/'+filecsv)
        print("Deleting png file from uniqcode "+UNIQCODE)
        os.system("rm -rf "+SRC_IMG+'/'+UNIQCODE+"*")
