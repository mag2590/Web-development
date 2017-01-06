
import os
import jinja2
import webapp2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
import utility
from Entities.entities import *
from google.appengine.ext import db
import logging

"""
User needs to be logged in to do this operation. Once logged in, if he clicks on the icon--> popup to ask for sure
Only then, delete the post from the database and remove it from the page.
1.
"""
class DeletePostHandler(MainHandler):

    def get(self, post_id, post_user_id):
        if self.user and self.user.key().id() == int(post_user_id):
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            logging.info(key)
            post = db.get(key)
            logging.info(post)
            post.delete()

            self.redirect('/blog/')

        elif not self.user:
            logging.info("Is it reaching here maybe??")
            self.redirect('/blog/login')

        else:
            logging.info("If not above it has to reach here!!")
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            comments = db.GqlQuery(
                "select * from Comment where ancestor is :1 order by created desc limit 10", key)

            error = "You don't have permission to delete this post"
            self.render("permalink.html", post=post, comments=comments, error=error)