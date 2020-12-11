#!/usr/bin/python3.8
from fpdf import FPDF
import os
from os import listdir
import sys
import csv
import subprocess


##FOR FILTER##
import glob

##FOR SEPARATE##
import re

#pdf = FPDF('P','mm','A4')
pdf = FPDF()


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
for imglist in LISTIMG:
    #subprocess.call(['/bin/grep', imglist])
    #print(imglist)
    #exit()
    pdf.add_page()
    pdf.cell(200, 10, txt=TITLE, ln=1, align="C")
    pdf.set_font("Arial", size=12)
    pdf.image(SRC_IMG+'/'+GTYPE+'/'+imglist, 0, 0)
pdf.output(TITLE+".pdf",)
pdf = FPDF(orientation='L', unit='mm')
