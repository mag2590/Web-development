
import os
import jinja2
import webapp2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
from Entities.entities import *
import logging

class LoginHandler(MainHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        logging.info(u)
        if u:
            self.login(u)
            self.redirect('/blog/newpost')
        else:
            error = "Invalid username or password, please provide the correct credentials"
            self.render('login.html',error=error)