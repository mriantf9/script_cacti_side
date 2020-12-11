#!/usr/bin/python3.8
from fpdf import FPDF
import os
from os import listdir
import sys
import csv
import subprocess
import fnmatch

##FOR FILTER##
import glob

##FOR SEPARATE##
import re

#pdf = FPDF('P','mm','A4')

cobain = "RO.JAK.IDM2 - Traffic - Te0/1/0.47"
haha = cobain.replace(" ", "_")
hehe = haha.replace("/", "-")

print(hehe)
exit()

###### DEFINE ######
DIR = "/home/mriantf/script_skripsi"
DT_DIR = DIR+"/DATA_REPORT"
SRC_IMG= DIR+"/OUTPUT"
OUTPUT_PDF = DIR+"/OUTPUT_PDF"
GTYPE = sys.argv[1]

LISTIMG = listdir(SRC_IMG+'/'+GTYPE)

csv_list = listdir(DT_DIR+'/'+GTYPE)

#print(csv_list)
list_img = ''
IDREPORT = ''
EMAIL = ''
TITLE = ''
RRDTITLE = ''
PERIODIC = ''

pdf = FPDF('P','mm','A4')

for filecsv in csv_list:
    with open (DT_DIR+'/'+GTYPE+'/'+filecsv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            IDREPORT = row[0]
            EMAIL = row[2]
            TITLE = row[3]
            RRDTITLE = row[6]
            RRDTITLE_RPL = RRDTITLE.replace(" ", "%temp%").replace("_", "-").replace("%temp%", "/")
            PERIODIC = row[7]
            #filelist = fnmatch.filter(os.listdir(SRC_IMG+'/'+GTYPE), "*ReportID"+IDREPORT+"*")
            filelist = fnmatch.filter(os.listdir(SRC_IMG+'/'+GTYPE), "*"+RRDTITLE_RPL+"*")
            count_array = len(filelist) + 1
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(190, 10, txt=TITLE, ln=1, align="C")
            for i in range(1, count_array):
                pdf.cell(0, 10, str(i) + '. Traffic Pemakaian ' + RRDTITLE, 0, 1)

pdf.output(TITLE+".pdf")
            

#print (filelist)

    #for imglist in filelist:
        # subprocess.call(['/bin/grep', imglist])
        # print(imglist)
        # exit()
        # count_array = len(filelist) + 1
        # pdf.add_page()
        # pdf.set_font("Arial", size=12)
        #pdf.cell(190, 10, txt=TITLE, ln=1, align="C")
        #pdf.image(SRC_IMG+'/'+GTYPE+'/'+imglist, 50, 50, 100)
        #for i  in range(1, count_array):
        #    pdf.cell(0, 10, str(i) + '. Traffic Pemakaian ' + RRDTITLE, 0, 1)
    #pdf.output(TITLE+".pdf")
