#!/usr/bin/python3.8

from fpdf import FPDF
from os import listdir
import sys
import csv

##FOR FILTER##
import glob

##FOR SEPARATE##
import re

###### DEFINE ######
DIR = "/home/mriantf/script_skripsi"
DT_DIR = DIR+"/DATA_REPORT"
SRC_IMG= DIR+"/OUTPUT"
OUTPUT_PDF = DIR+"/OUTPUT_PDF"
GTYPE = sys.argv[1]

LISTIMG = listdir(SRC_IMG)

csv_list = listdir(DT_DIR+'/'+GTYPE)

print(csv_list)


# pdf = FPDF('P','mm','A4')
# pdf.add_page()
# pdf.set_font("Arial", size=12)

# ### TEXT CENTER ###
# pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")












### OUTPUT ###
# pdf.output("/mnt/d/LARAVEL/simple_demo.pdf")



