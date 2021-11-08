import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('xxx@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Daxxxd'
msg['To'] = 'xxx@gmail.com'
msg['Subject'] = 'Test message'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = '<filename>'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

try:
    server.sendmail('xxx@gmail.com', 'xxx@gmail.com', text)
    print("Succenssfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")