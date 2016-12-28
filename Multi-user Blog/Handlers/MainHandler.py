import webapp2
import os
import jinja2
from Entities.entities import Post
import utility
#setup jinja environment variable

class MainHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a,**kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(utility.render_str(template,**kw))

