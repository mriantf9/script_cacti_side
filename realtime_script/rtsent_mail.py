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
DIR = "/home/mriantf/script_skripsi/REALTIME"
SRC_IMG= DIR+"/OUTPUT"
OUTPDF = DIR+"/OUTPUT_PDF"
EMAIL = sys.argv[1]
FILEPDF = sys.argv[2]
UNIQCODE = sys.argv[3]

fromaddr = "sentpython@gmail.com"
toaddr = EMAIL
cc = "fajaryanto.riant@gmail.com"
toaddrs = toaddr+cc

 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Cc'] = cc
msg['Subject'] = "[DO NOT REPLY] - REPORT GRAPHIC UTILIZATION " + UNIQCODE

 
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
attachment = open(OUTPDF+'/'+FILEPDF, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "@Testing@10")
text = msg.as_string()
server.sendmail(fromaddr, toaddrs, text)
server.quit()


print('Mail Sent')
