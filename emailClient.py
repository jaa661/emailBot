import smtplib
import creds
import time
import imaplib
import json
import email
import easyimap
import smtplib
import apiai
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def receiveIMAP():
    imapper = easyimap.connect('imap.gmail.com', creds.login, creds.password)
    for mail_id in imapper.listids(limit=100):
        mail = imapper.mail(mail_id)
        print(mail.from_addr)
        #print(mail.to)
        #print(mail.cc)
        print('Title' + mail.title)
        print(mail.body)
        #print(mail.attachments)
        print('////////////////////////////////////////////////////////////////////////')

def sendEmailAsText(TEXT):

    msg = MIMEMultipart()
    msg['From'] = creds.sender
    msg['To'] = ", ".join(creds.receivers)

    # Simple text message or HTML
    msg.attach(MIMEText(TEXT))

    # Send the message
    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(login, password)
    smtpObj.sendmail(creds.sender, creds.receivers, msg.as_string())

def sendEmailAsTextCustom(TEXT, to, via):

    msg = MIMEMultipart()
    msg['From'] = creds.sender
    #msg['To'] = ", ".join(to)

    # Simple text message or HTML
    msg.attach(MIMEText(TEXT))

    # Send the message
    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(creds.login, creds.password)
    smtpObj.sendmail(creds.sender, to, msg.as_string())

def generateResponse(msg):
    if(msg.find('colors')!=-1):
        return "purple, green, and gold"
    else:
        return "I don't understand, sorry"

def generateAPIAIResponse(msg_from, msg):
    CLIENT_ACCESS_TOKEN = creds.CLIENT_ACCESS_TOKEN
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    # prepare API.ai request
    req = ai.text_request()
    req.lang = 'en'  # optional, default value equal 'en'
    req.query = msg

    # get response from API.ai
    api_response = req.getresponse()
    responsestr = api_response.read().decode('utf-8')
    response_obj = json.loads(responsestr)
    if 'result' in response_obj:
        response = response_obj["result"]["fulfillment"]["speech"]
        # send SMS response back
        return response


def autoReply():
    index = 0
    while True:
        #print('attempt #' + str(index))
        imapper = easyimap.connect('imap.gmail.com', creds.login, creds.password)
        for mail in imapper.unseen(100):
            #mail = imapper.mail(mail_id)
            print(mail.from_addr)
            print(mail.to)
            print('Title' + mail.title)
            print(mail.body)
            print('//////////////////////////')
            print('attempting')
            #TEXT = generateResponse(mail.body)
            TEXT = generateAPIAIResponse(mail.from_addr, mail.body)
            sendEmailAsTextCustom(TEXT, mail.from_addr, mail.to)
            print('response:')
            print(TEXT)
            print('text sent!!!!')
            print('////////////////////////////////////////////////////////////////////////')

        time.sleep(.5)
        index+=1
    
def main():
    print('works')
    autoReply()

main()
