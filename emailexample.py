import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os

login = 'trashLambda@gmail.com'
password = 'Thu361909'
sender = 'trashLambda@gmail.com'
receivers = ['pierules53@gmail.com','8184416085@vzwpix.com']

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ", ".join(receivers)
msg['Subject'] = "8=D Alert"

# Simple text message or HTML
TEXT = "Hello,\n"
TEXT = TEXT + "\n"
TEXT = TEXT + "ayyy lmao.\n"
TEXT = TEXT + "\n"
TEXT = TEXT + "Thanks,\n"
TEXT = TEXT + "Sent from Jacob's Pi"

msg.attach(MIMEText(TEXT))

filenames = ["test.txt"]
for file in filenames:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(file, 'rb').read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"'
                    % os.path.basename(file))
    msg.attach(part)

smtpObj = smtplib.SMTP('smtp.gmail.com:587')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(login, password)
smtpObj.sendmail(sender, receivers, msg.as_string())
