import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class MailW(object):
    def __init__(self, smtp_server='localhost',
                 smtp_port=587,
                 mail_sender='localhost@localhost.com',
                 mail_sender_passwd='*****',
                 mail_recipients=['localhost@localhost.com'],
                 subject='No subject',
                 text=None,
                 html=None):
        self.msg = MIMEMultipart('alternative')  # Must be positioned first
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.mail_sender = mail_sender
        self.mail_sender_passwd = mail_sender_passwd
        self.mail_recipients = mail_recipients
        self.subject = subject
        self.text = text
        self.html = html

    def add_attachments(self, filepaths):
        for filepath in filepaths:
            f = filepath
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(f, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            self.msg.attach(part)

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, html):
        if html is not None:
            self._html = html
            self.msg.attach(MIMEText(html, 'html'))

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if text is not None:
            self._text = text
            self.msg.attach(MIMEText(text, 'plain'))

    def __call__(self, *args, **kwargs):
        self.__dict__.update(**kwargs)
        self.msg['Subject'] = self.subject
        self.msg['To'] = ', '.join(self.mail_recipients)
        self.msg['From'] = self.mail_sender

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.mail_sender, self.mail_sender_passwd)
        server.send_message(self.msg)
        server.quit()