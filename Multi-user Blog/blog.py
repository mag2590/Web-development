#This file will be the calling point for the application and will contain
#all the handlers

import webapp2
import jinja2
import os
from Handlers.NewpostHandler import NewpostHandler
from Handlers.BlogHandler import BlogHandler
from Handlers.LoginHandler import LoginHandler
from Handlers.SignupHandler import SingupHandler
from Handlers.LogoutHandler import LogoutHandler
from google.appengine.ext import db
from string import letters
import utility

app = webapp2.WSGIApplication([('/blog/?', BlogHandler),
                               ('/blog/login', LoginHandler),
                               ('/blog/newpost', NewpostHandler),
                               ('/blog/signup', SingupHandler),
                               ('/blog/logout', LogoutHandler)
                               ], debug=True)



