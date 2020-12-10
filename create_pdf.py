#!/usr/bin/python3.8

from fpdf import FPDF
from os import listdir
import sys

###### DEFINE DIRECTORY ######
DIR = "/home/mriantf/script_skripsi"
SRC_IMG= DIR+"/OUTPUT"
OUTPUT_PDF = DIR+"/OUTPUT_PDF"


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

### TEXT CENTER ###
pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")












### OUTPUT ###
pdf.output("/mnt/d/LARAVEL/simple_demo.pdf")



