import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from djangoPersonalWebPage.settings import EMAIL_SETTINGS

port = 587  # For starttls
smtp_server = EMAIL_SETTINGS['smtp_server']
sender_email = EMAIL_SETTINGS['sender_email']
password = EMAIL_SETTINGS['password']


def sendmail(body, target=EMAIL_SETTINGS['target']):
    receiver_email = target
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Nate Astrup"
    message.attach(MIMEText(body, "plain"))
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
