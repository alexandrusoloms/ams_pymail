import os
import smtplib

EMAIL_CREDENTIALS = os.environ['Mail']


def send_mail(subject, body, to_address):
    """
    sends an email notification when a script breaks

    :param subject: the title of the email
    :param body: the main message of the email
    :param to_address: the email that receives the error
    :return:
    """

    from_address, pwd = EMAIL_CREDENTIALS.split()
    from_address = from_address + '@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(from_address, pwd)

    message = 'Subject: {}\n\n{}'.format(subject, body)
    server.sendmail(from_address, to_address, message)
