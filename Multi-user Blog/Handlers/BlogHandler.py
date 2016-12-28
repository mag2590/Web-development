import os
import webapp2
import jinja2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
from Entities.entities import Post
import utility


class BlogHandler(MainHandler):
    def get(self):
        #get and render all the posted blogs by a user
        posts = Post.all().order('-created_at')
        self.render("blog.html",posts=posts)

