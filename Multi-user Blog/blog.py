#This file will be the calling point for the application and will contain
#all the handlers

import webapp2
import jinja2
import os
from Handlers.NewpostHandler import NewpostHandler
from Handlers.BlogHandler import BlogHandler
from Handlers.LoginHandler import LoginHandler
from Handlers.PostHandler import PostHandler
from Handlers.SignupHandler import SingupHandler
from Handlers.LogoutHandler import LogoutHandler
from Handlers.EditPostHandler import EditPostHandler
from Handlers.DeletePostHandler import DeletePostHandler
from Handlers.UserPostsHandler import UserPostsHandler
from Handlers.LikePostHandler import LikePostHandler
from Handlers.NewCommentHandler import NewCommentHandler
from Handlers.EditCommentHandler import EditCommentHandler
from Handlers.DeleteCommentHandler import DeleteCommentHandler
from google.appengine.ext import db
from string import letters
import utility

app = webapp2.WSGIApplication([('/blog/?', BlogHandler), #mainpage
                               ('/blog/login', LoginHandler), #sign in after signup/or existing user
                               ('/blog/newpost', NewpostHandler),
                               ('/blog/([0-9]+)',PostHandler), #after login newpost
                               ('/blog/signup', SingupHandler), # new user signup page
                               ('/blog/logout', LogoutHandler), #after login- logout.
                               ('/blog/([0-9]+)/edit', EditPostHandler), #edit a post after a user is logged in
                               ('/blog/([0-9]+)/delete/([0-9]+)',DeletePostHandler),
                               ('/blog/([0-9]+)/userpost', UserPostsHandler),
                               ('/blog/([0-9]+)/like', LikePostHandler),
                               ('/blog/([0-9]+)/newcomment/([0-9]+)',NewCommentHandler),
                               ('/blog/([0-9]+)/editcomment/([0-9]+)', EditCommentHandler),
                               ('/blog/([0-9]+)/deletecomment/([0-9]+)', DeleteCommentHandler)
                               ], debug=True)



