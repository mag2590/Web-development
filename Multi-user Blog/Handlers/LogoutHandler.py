
import os
import jinja2
import webapp2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
import utility

class LogoutHandler(MainHandler):
    #Clear/expire the cookie and redirect to the main page.
    def clear_cookie(self):
        self.response.headers.add_header('Set-Cookie','user_id=; Path=/')

    def get(self):
        self.clear_cookie()
        logged_out = True
        self.render('login.html',logged_out=logged_out)