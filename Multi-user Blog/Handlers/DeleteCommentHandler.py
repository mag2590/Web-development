from google.appengine.ext import db
from utility import *
from Handlers.MainHandler import MainHandler

class DeleteCommentHandler(MainHandler):

    def get(self, post_id, post_user_id, comment_id):

        if self.user and self.user.key().id() == int(post_user_id):
            postKey = db.Key.from_path('Post', int(post_id), parent=blog_key())
            key = db.Key.from_path('Comment', int(comment_id), parent=postKey)
            comment = db.get(key)
            comment.delete()

            self.redirect('/blog/' + post_id)

        elif not self.user:
            self.redirect('/blog/login')

        else:
            self.write("You cannot delete this comment because you did not write it!!")