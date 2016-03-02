#!/usr/bin/python

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib

class Emailer:

    def __init__(self, meals):
        self.meals     = meals
        self.to_addr   = 'lordkimber@gmail.com'
        self.from_addr = 'lordkimber@gmail.com'

    def get_message(self):
        string = ''
        for meal in self.meals:
            string = meal.show(string)
            string = string + '\n'

        message = MIMEText(string, 'plain')
        message['to'] = self.to_addr
        message['From'] = self.from_addr
        message['Subject'] = 'Shopping list'

        return message

    def send_list(self):
        username = 'lordkimber@gmail.com'
        password = self.get_password()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(self.from_addr, self.to_addr, self.get_message().as_string())
        server.quit()

    def get_password(self):
        return open(os.path.dirname(__file__) + '/../secrets/password').read()
