"""
This file will contain all the entities required for Blog app
"""
from google.appengine.ext import db

import utility
import logging


def users_key(group='default'):
    return db.Key.from_path('users', group)


#Put the new blog in the database associate it to a key
def blog_key(name='default'):
    return db.Key.from_path('blogs',name)

class User(db.Model):
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def register(cls, name, pw, email=None):
        pw_hash = utility.make_pw_hash(name, pw)
        return User(parent=users_key(),
                    name=name,
                    pw_hash=pw_hash,
                    email=email)

    @classmethod
    def login(cls, username, password):
        u = User.by_name(username)
        if u and utility.validate_pw(username, password, u.pw_hash):
            return u

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent=users_key())

    @classmethod
    def by_name(cls, name):
        u = User.all().filter('name =', name).get()
        return u


class Post(db.Model):
    """
    Entity to store a Blog Post.
    """
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    picture = db.BlobProperty()
    user_id = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    likes = db.IntegerProperty(default=0)

    def render(self,current_user_id):
        #get key from the database
        key = db.Key.from_path('User', int(self.user_id),parent=users_key())
        user = db.get(key)
        self._render_text = self.content.replace('\n', '<br>')
        return utility.render_str("post.html", p=self, current_user_id=current_user_id, author = user.name)

    @classmethod
    def by_id(cls, uid):
        return Post.get_by_id(uid, parent=blog_key())


class Like(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    user_id = db.IntegerProperty(required=True)
    post_id = db.IntegerProperty(required=True)


class Comment(db.Model):
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    user_id = db.IntegerProperty(required=True)
    user_name = db.TextProperty(required=True)