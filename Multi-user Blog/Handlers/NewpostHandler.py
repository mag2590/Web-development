
import os
import jinja2
import webapp2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
import utility
from Entities.entities import *
import logging

class NewpostHandler(MainHandler):

    def get(self):
        if self.user:
            logging.info(self.user)
            self.render("newpost.html")
        else:
            error = "You must be signed in to create a post."
            self.render("base.html", access_error=error)


    def post(self):
        if not self.user:
            return self.redirect('/login')
        subject = self.request.get('subject')
        content = self.request.get('content')
        if subject and content:
            p = Post(parent=blog_key(), subject=subject,
                     content=content,user_id=self.user.key().id())
            p.put()
            logging.info(p.key().id())
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "Are you day dreaming, what do you want me to post?? Please fill up both subject and content before submitting!!"
            self.render("newpost.html",subject=subject, content=content, error=error)
