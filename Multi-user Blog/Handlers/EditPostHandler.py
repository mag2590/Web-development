import os
import jinja2
import webapp2
import Handlers.MainHandler
from Handlers.MainHandler import MainHandler
import utility
from Entities.entities import *
import logging

# When clicked on the content on post page the current content should not be lost
# It should be a link to the newpost and keep the current contents in the newpost page.


class EditPostHandler(MainHandler):
    def get(self,post_id):
        #retrieve the post to be edited for this user from the database
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        logging.info(key)
        post=db.get(key)

        #validate the user for this post before allowing to edit
        if self.user and self.user.key().id() == post.user_id:
            self.render('editpost.html', subject=post.subject,
                        content=post.content, post_id=post_id)

        elif not self.user:
            self.redirect('/blog/login')

        else:
            self.write("You are not authorized to edit other's posts!")

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not self.user:
            return self.redirect('/blog/login')

        if self.user and self.user.key().id() == post.user_id:
            subject = self.request.get('subject')
            content = self.request.get('content')

            if subject and content:
                key = db.Key.from_path('Post', int(post_id), parent=blog_key())
                post = db.get(key)

                post.subject = subject
                post.content = content

                post.put()

                self.redirect('/blog/%s' % str(post.key().id()))
            else:
                error = "subject and content, bitch!"
                self.render("newpost.html", subject=subject,
                            content=content, error=error)

        else:
            self.write("You are not authorized to edit other's posts!")