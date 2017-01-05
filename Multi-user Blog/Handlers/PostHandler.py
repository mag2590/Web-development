import os
import webapp2
import jinja2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
from Entities.entities import *
from google.appengine.ext import db
import utility


class PostHandler(MainHandler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html",post=post)
