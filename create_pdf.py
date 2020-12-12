#!/usr/bin/python3.8
from fpdf import FPDF
import os
from os import listdir
import sys
import csv
import subprocess
import fnmatch
import datetime

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

today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
LAST_MONTH = lastMonth.strftime("%B %Y")


list_img = ''
IDREPORT = ''
EMAIL = ''
TITLE = ''
RRDTITLE = ''
PERIODIC = ''

for filecsv in csv_list:
    pdf = FPDF('L','mm','Letter')
    with open (DT_DIR+'/'+GTYPE+'/'+filecsv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        #line_count = 0
        for row in csv_reader:
            IDREPORT = row[0]
            EMAIL = row[2]
            TITLE = row[3]
            RRDTITLE = row[6]
            RRDTITLE2 = RRDTITLE.replace(" ", "_")
            RRDTITLE3 = RRDTITLE2.replace("/","-")
            PERIODIC = row[7]
            filelist = fnmatch.filter(os.listdir(SRC_IMG+'/'+GTYPE), "*"+RRDTITLE3+"*")
            
            count_array = len(filelist) + 1
            idx = 1
            for imglist in filelist:
                path = SRC_IMG+'/'+GTYPE+'/'+imglist
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(250, 20, txt=TITLE, ln=6, align="C")
                pdf.cell(0, 30, str(idx) + '. Traffic Pemakaian ' + RRDTITLE, 0, 1)
                pdf.ln(10)
                pdf.image(SRC_IMG+'/'+GTYPE+'/'+imglist, 45, 60, 190, 80)
                idx += 1
    pdf.output(OUTPUT_PDF+'/'+GTYPE+'/'+"ReportID"+IDREPORT+"_"+TITLE+".pdf")
            

