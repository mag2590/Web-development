
import os
import jinja2
import webapp2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
from utility import *
import Entities.entities

class LoginHandler(MainHandler):
    def get(self):
        self.render("login.html")

    def set_cookie(self, username):
        cookie_val = utility.make_secure_key(username)
        return cookie_val and utility.check_secure_key(cookie_val)

    def read_cookie(self, username):
        #use the
        cookie_val = self.request.cookies.get(username)
        return cookie_val and utility.check_secure_key(cookie_val)

    def login(self, username):
        self.set_cookie('username', str(username.key().id()))