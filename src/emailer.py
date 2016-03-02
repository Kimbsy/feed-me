#!/usr/bin/python

import os
import smtplib

class Emailer:

    def __init__(self, meals):
        self.meals     = meals
        self.message   = self.get_message()
        self.to_addr   = 'dave.kimber@simitive.com'
        self.from_addr = 'lordkimber@gmail.com'

    def get_message(self):
        string = ''
        for meal in self.meals:
            string = meal.show(string)
            string = string + '\n'

        return string

    def send_list(self):
        username = 'lordkimber@gmail.com'
        password = self.get_password()

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(self.from_addr, self.to_addr, self.message)
        server.quit()

    def get_password(self):
        return open(os.path.dirname(__file__) + '/../secrets/password').read()
