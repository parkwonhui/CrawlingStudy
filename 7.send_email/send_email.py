import smtplib, os, pickle
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64
import time

id = ''
password = ''
sendEmail = ''
subject = 'testMail'
text = 'hello world~!'
addrs = [sendEmail] 		# send mail list

# login
smtp = smtplib.SMTP('smtp.naver.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(id, password)

# message
message = MIMEMultipart()
message.attach(MIMEText(text))

# Send
for addr in addrs:
	message["From"] = sendEmail
	message["To"] = addr
	message['Subject'] = subject
	smtp.sendmail(sendEmail, addr, message.as_string())

smtp.quit()
