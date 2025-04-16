from os import getenv
from dotenv import load_dotenv
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List


class Mail:
    def __init__(self, smtp: str, imap: str, port=587, psw=''):
        self.smtp = smtp
        self.imap = imap
        self.port = port
        self.psw = psw

    def send(self, from_email: str, to_emails: List[str], message_: MIMEMultipart):
        ms = smtplib.SMTP(self.smtp, self.port)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(from_email, self.psw)
        ms.sendmail(from_email, to_emails, message_.as_string())
        ms.quit()

    def receive(self, receive_email, header_='', box='inbox'):
        mails = imaplib.IMAP4_SSL(self.imap)
        mails.login(receive_email, self.psw)
        mails.list()
        mails.select(box)
        criterion = '(HEADER Subject "%s")' % header_ if header_ else 'ALL'
        result, data = mails.uid('search', None, criterion)
        if not data:
            return None

        latest_email_uid = data[0].split()[-1]
        result, data = mails.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = (data[0][1])

        email_message = email.message_from_bytes(raw_email)
        mails.logout()
        return email_message


if __name__ == '__main__':
    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"
    load_dotenv()
    password = getenv('psw')

    mail = Mail(gmail_smtp, gmail_imap, psw=password)

    mailer = 'nicansh@gmail.com'
    # recipients = ['vasya@email.com', 'petya@email.com']
    recipients = ['nshmv@mail.ru']
    subject = 'Subject'
    message = 'Message'
    header = None

    msg = MIMEMultipart()
    msg['From'] = mailer
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    mail.send(mailer, recipients, msg)

    letter = mail.receive(mailer)
    if letter:
        print(letter)
    else:
        print('No mail')
