
import os
import jinja2
import webapp2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
import utility
from Entities.entities import Post, User


class NewpostHandler(MainHandler):

    def get(self):
        self.render('newpost.html')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            #user_obj = User.get_by_id(int(self.user))
            p = Post(parent=blog_key(), subject=subject, content=content)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content bitch!"
            self.render("newpost.html",subject=subject, content=content, error=error)
