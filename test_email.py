
import smtplib # pip3 install smtplib
import imaplib # pip3 install imaplib

TO = 'recipient@mailservice.com' # шапка письма
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'


gmail_sender = 'aarrtt996@gmail.com' # email
gmail_passwd = 'az0922201625' # password

server = smtplib.SMTP('smtp.gmail.com', 587) # connected to port 587(SMTP) to email
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd) # connected to you

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT]) # print your massege

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit() # завершение сессии
