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
pdf = FPDF('P','mm','A4')


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


for filecsv in csv_list:
    with open (DT_DIR+'/'+GTYPE+'/'+filecsv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                IDREPORT = row[0]
                EMAIL = row[1]
                TITLE = row[3]
                RRDTITLE = row[6]
                PERIODIC = row[7]
            else:
                break
#list_img = [os.system("ls "+SRC_IMG+'/'+GTYPE+"| grep ReportID"+IDREPORT)]

filelist = fnmatch.filter(os.listdir(SRC_IMG+'/'+GTYPE), "*ReportID"+IDREPORT+"*")

print (filelist)

#for imglist in LISTIMG:
    #subprocess.call(['/bin/grep', imglist])
    #print(imglist)
    #exit()
<<<<<<< HEAD
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=TITLE, ln=1, align="C")
    pdf.image(SRC_IMG+'/'+GTYPE+'/'+imglist, 50, 50, 100)
    for i  in range(1,50):
       pdf.cell(0, 10, 'Cell Number ' + str(i), 0, 1)
pdf.output(TITLE+".pdf", 'F')
=======
#    pdf.add_page()
#    pdf.set_font("Arial", size=12)
#    pdf.cell(200, 10, txt=TITLE, ln=1, align="C")
#    pdf.image(SRC_IMG+'/'+GTYPE+'/'+imglist, 50, 50, 100)
#    for i  in range(1,50):
#       pdf.cell(0, 10, 'Cell Number ' + str(i), 0, 1)
#pdf.output(TITLE+".pdf", 'F')
>>>>>>> d8e30a984ad0254dec7365d681cc89310e46e2ed
