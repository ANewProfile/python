import smtplib
from email.message import EmailMessage
import keys

def send_email(sender, password, to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = subject

    # connect to gmail
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    # send an email!
    send_email(
        keys.sender_email,
        keys.app_password,
        'cheo.door@gmail.com',
        'hey there!',
        'this is the email body 🌟'
    )