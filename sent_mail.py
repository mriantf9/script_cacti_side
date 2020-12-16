#!/usr/bin/python3.8

from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from os import listdir
import sys

###### DEFINE ######
DIR = "/home/mriantf/script_skripsi"
DT_DIR = DIR+"/DATA_REPORT"
SRC_IMG= DIR+"/OUTPUT"
OUTPUT_PDF = DIR+"/OUTPUT_PDF"
EMAIL = sys.argv[1]
FILEPDF = sys.argv[2]
GTYPE = sys.argv[3]

fromaddr = "sentpython@gmail.com"
toaddr = EMAIL

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
LAST_24HOURS = last_24.strftime("%d %B %Y %H:%M:%S")
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
if GTYPE == "Monthly":
    msg['Subject'] = "[DO NOT REPLY] - REPORT GRAPHIC UTILIZATION " + LAST_MONTH
elif GTYPE == "Weekly":
    msg['Subject'] = "[DO NOT REPLY] - REPORT GRAPHIC UTILIZATION " + LAST_WEEK + " TO " + tdy
else:
    msg['Subject'] = "[DO NOT REPLY] - REPORT GRAPHIC UTILIZATION " + LAST_24HOURS

 
body = '''Dear Customer,
As I attached, Report Utilization from your service.

If you need detail question, Feel free to contact our support

Email: support@riantf.id
Phone: +6221 - 8829-0123-00

Thank You,
Best Regards

Your Support
'''
 
msg.attach(MIMEText(body, 'plain'))
# Lampiran, sesuaikan nama filename dengan nama di attachment
filename = FILEPDF
attachment = open(OUTPUT_PDF+'/'+GTYPE+'/'+FILEPDF, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "@Testing@10")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


print('Mail Sent')
