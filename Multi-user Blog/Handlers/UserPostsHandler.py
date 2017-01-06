import os
import webapp2
import jinja2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
from Entities.entities import *
from google.appengine.ext import db
import utility


class UserPostsHandler(MainHandler):
    def get(self,userid):
        if self.user:
            posts = db.GqlQuery(
                "select * from Post where user_id =:userid  order by created desc",userid=int(userid))
            self.render("userpost.html", posts=posts)