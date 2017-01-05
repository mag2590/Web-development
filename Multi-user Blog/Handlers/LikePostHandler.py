from google.appengine.ext import db
from Handlers.MainHandler import MainHandler
from utility import *
from Entities.entities import *

class LikePostHandler(MainHandler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user and self.user.key().id() == post.user_id:
            error = "You cannot like your own post!!!"
            self.render('base.html', access_error=error)
        elif not self.user:
            self.redirect('/blog/login')
        else:
            user_id = self.user.key().id()
            post_id = post.key().id()

            like = Like.all().filter('user_id =', user_id).filter('post_id =', post_id).get()

            if like:
                self.redirect('/blog/' + str(post.key().id()))

            else:
                like = Like(parent=key,
                            user_id=self.user.key().id(),
                            post_id=post.key().id())

                post.likes += 1

                like.put()
                post.put()

                self.redirect('/blog/' + str(post.key().id()))