import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os

login = 'trashLambda@gmail.com'
password = 'Thu361909'
sender = 'trashLambda@gmail.com'
receivers = ['8184416085@vzwpix.com']

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ", ".join(receivers)

# Simple text message or HTML
TEXT = '''ayyy lmao
Sent from Jacob's Pi'''
msg.attach(MIMEText(TEXT))

# Send the message
smtpObj = smtplib.SMTP('smtp.gmail.com:587')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(login, password)
smtpObj.sendmail(sender, receivers, msg.as_string())
