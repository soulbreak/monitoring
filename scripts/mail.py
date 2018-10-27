from src.packages.com.mail import Mail_w

if __name__ == '__main__':
    from config.mail import smtp_server, smtp_port, mail_sender, mail_recipients, mail_sender_passwd

    mymail = Mail_w(smtp_server=smtp_server,
                  smtp_port=smtp_port,
                  mail_sender=mail_sender,
                  mail_recipients=mail_recipients,
                  mail_sender_passwd=mail_sender_passwd)

    filepaths = [r'mail.py',
                r'__init__.py']
    """Send the contents of a directory as a MIME message."""

    html = """
<html>
    <p>This is some HTML</p>
    <b>Cool</b>
</html>"""

    mymail.html = html
    mymail.text = 'coucou'
    mymail.add_attachments(filepaths)
    mymail()


