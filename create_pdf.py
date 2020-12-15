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

#pdf = FPDF('P','mm','A4')

###### DEFINE ######
DIR = "/home/mriantf/script_skripsi"
DT_DIR = DIR+"/DATA_REPORT"
SRC_IMG= DIR+"/OUTPUT"
OUTPUT_PDF = DIR+"/OUTPUT_PDF"
GTYPE = sys.argv[1]

LISTIMG = listdir(SRC_IMG+'/'+GTYPE)

csv_list = listdir(DT_DIR+'/'+GTYPE)


##################################
######## LAST MONTH ##############
##################################
TODAY = datetime.now()
lastMonth = TODAY - timedelta(days=31)
LAST_MONTH = lastMonth.strftime("%d %B %Y")

tdy = TODAY.strftime("%d %B %Y")

#################################
######### LAST WEEK #############
#################################
last_7day = datetime.now() - timedelta(days=7)
LAST_WEEK = last_7day.strftime("%d %B %Y")

#################################
######### LAST 24 #############
#################################
last_24 = datetime.now() - timedelta(hours=24)
LAST_24HOURS = last_24.strftime("%d %B %Y")


list_img = ''
IDREPORT = ''
EMAIL = ''
TITLE = ''
RRDTITLE = ''
PERIODIC = ''
REPORT = ''

for filecsv in csv_list:
    pdf = FPDF('L','mm','Letter')
    with open (DT_DIR+'/'+GTYPE+'/'+filecsv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        #line_count = 0
        for row in csv_reader:
            IDREPORT = row[0]
            EMAIL = row[2]
            TITLE = row[3]
            PDFNAME = TITLE.replace(" ", "_")
            RRDTITLE = row[6]
            RRDTITLE2 = RRDTITLE.replace(" ", "_")
            RRDTITLE3 = RRDTITLE2.replace("/","-")
            PERIODIC = row[7]
        
        REPORT = "ReportID"+IDREPORT
        filelist = fnmatch.filter(os.listdir(SRC_IMG+'/'+GTYPE), "*"+REPORT+"*")

            
        #count_array = len(filelist) + 1
        idx = 1
        for imglist in filelist:
            path = SRC_IMG+'/'+GTYPE+'/'+imglist
            pdf.add_page()
            pdf.set_font("Times", size=15)
            pdf.cell(250, 20, txt=TITLE, ln=1, align="C")
            if GTYPE == "Monthly":
                pdf.cell(250, 2, "From "+str(LAST_MONTH)+" - "+str(tdy), ln=2, align="C")
            elif GTYPE == "Weekly" :
                pdf.cell(250, 2, "From "+str(LAST_WEEK)+" - "+str(tdy), ln=2, align="C")
            else:
                pdf.cell(250, 2, "From "+ str(LAST_24HOURS)+" - "+str(tdy), ln=2, align="C")
            pdf.ln(3)
            pdf.cell(250, 10, txt="Periodic Graph Capture - per"+PERIODIC, ln=1, align="C")
            pdf.cell(0, 20, str(idx) + '. Traffic Pemakaian ' + RRDTITLE, 0, 1)
            pdf.ln(10)
            pdf.image(SRC_IMG+'/'+GTYPE+'/'+imglist, 45, 65, 190, 80)
            idx += 1
    pdf.output(OUTPUT_PDF+'/'+GTYPE+'/'+"ReportID"+IDREPORT+"_"+PDFNAME+".pdf")



PDFLIST = listdir(OUTPUT_PDF+'/'+GTYPE)
for PDFFILELIST in PDFLIST:
    os.system('/usr/bin/python3.8 '+DIR+'/script sent_mail.py ' +EMAIL+" "+PDFFILELIST+" "+GTYPE)


            

# try:
#     os.system("rm -rf "+DT_DIR+'/'+GTYPE+'/*')
#     os.system("rm -rf "+DT_DIR+'/'+GTYPE+'/* | grep '+REPORT)
# except OSError as e:
#     print("Error: %s : %s" % (SRC_IMG+'/'+GTYPE, e.strerror))
