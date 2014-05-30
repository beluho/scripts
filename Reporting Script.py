#!/usr/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import MySQLdb
import csv
import StringIO
import datetime
import time

datestr = time.strftime("%Y%m%d")

# Variables
gmail_user = "FROM EMAIL ADDRESS"
gmail_pwd = "PASSWORD"
subject_line = "DESIRED SUBJECT LINE"
report_name = "DESIRED REPORT NAME HERE"
report_query = """

YOUR 
QUERY
GOES
HERE ;

"""

# Open database connection
db = MySQLdb.connect(host="####",port= ####,user="####",passwd="#####",db="####" )

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Execute Query
cursor.execute(report_query)

# Write to CSV File & Append Datestring to name


csv_writer = csv.writer(open((report_name+datestr+".csv"), "wt")) 
csv_writer.writerow([i[0] for i in cursor.description]) # write headers
csv_writer.writerows(cursor)
del csv_writer # this will close the CSV file

fh = open("24_hour_sales_"+datestr+".csv", "r")
csv = fh.read()
print csv

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   mailServer.close()

# Send Mail
mail(recipient_email,
   subject_line,
   csv,
   report_name+datestr+".csv")

# disconnect from server
db.close()
