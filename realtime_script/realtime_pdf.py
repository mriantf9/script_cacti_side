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
csv_list=WORKDIR+"/data_list"
UNIQCODE = sys.argv[1]

print(UNIQCODE)
exit()