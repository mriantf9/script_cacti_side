#!/usr/bin/python3.8


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
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "[DO NOT REPLY] - REPORT GRAPHIC UTILIZATION"
 
body = '''Dear Customer,
As I attached, Report Utilization from your service.

If you need more detail question, Please contact our support

Email: support@riantf.id
Phone: +6221 - 8829-0123-00

Thank You,
Best Regards

Your Support
'''
 
msg.attach(MIMEText(body, 'plain'))
# Lampiran, sesuaikan nama filename dengan nama di attachment
filename = FILEPDF
attachment = open(OUTPUT_PDF+'/'+GTYPE, "rb")
 
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
