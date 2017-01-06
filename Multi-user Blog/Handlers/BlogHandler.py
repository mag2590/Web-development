import os
import webapp2
import jinja2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
from Entities.entities import Post
import utility
from google.appengine.ext import db


class BlogHandler(MainHandler):
    def get(self):
        posts = db.GqlQuery(
            "select * from Post order by created desc limit 10")
        self.render("blog.html",posts=posts)
