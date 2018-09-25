import smtplib
import time
import imaplib
import email
import easyimap

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "trashLambda" + ORG_EMAIL
FROM_PWD    = "Thu361909"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email_from_gmail():
    print("trying to read emails")
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()   
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])


    for i in range(latest_email_id,first_email_id, -1):
        typ, data = mail.fetch(i, '(RFC822)' )

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                email_subject = msg['subject']
                email_from = msg['from']
                print('From : ' + email_from + '\n')
                print('Subject : ' + email_subject + '\n')




def read_email_from_gmail2():
    print("trying to read emails")

    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)
    mail.list()
    mail.select('inbox')

    result, data = mail.search(None, "ALL")
 
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    latest_email_id = id_list[-1] # get the latest
 
    result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
    raw_email = data[0][1] # here's the body, which is raw text of the whole email
    # including headers and alternate payloads

    raw_email = data[0][1]
    email_message = email.message_from_string(str(raw_email))

    print (email_message['To'])

    print (email.utils.parseaddr(email_message['From'])) # for parsing "Yuji Tomita" <yuji@grovemade.com>

    print (email_message.items()) # print all headers





def get_first_text_block(self, email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()


def receiveIMAP():
    login = 'trashLambda@gmail.com'
    password = 'Thu361909'

    imapper = easyimap.connect('imap.gmail.com', login, password)
    for mail_id in imapper.listids(limit=100):
        mail = imapper.mail(mail_id)
        print(mail.from_addr)
        #print(mail.to)
        #print(mail.cc)
        print('Title' + mail.title)
        print(mail.body)
        #print(mail.attachments)
        print('////////////////////////////////////////////////////////////////////////')


    
def main():
    print('works')

main()
