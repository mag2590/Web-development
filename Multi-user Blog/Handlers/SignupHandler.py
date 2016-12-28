
import os
import jinja2
import webapp2
from Handlers.MainHandler import MainHandler
import utility

class SingupHandler(MainHandler):
    def get(self):
        self.render("signup.html")

    def done(self,*a,**kw):
        raise NotImplementedError

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify_pass = self.request.get('verify_password')
        email = self.request.get('email')

        #validate and redirect accordingly
        if not utility.valid_username(username):
            self.response.out.write('Invalid username!!')
        elif not utility.valid_password(password):
            self.response.out.write('Invalid password!!')
        elif password != verify_pass:
            self.response.out.write('Passwords did not match!')
        elif not utility.valid_email(email):
            self.response.out.write('Please enter valid email address!')
        else:
            self.render("welcome.html",username=username)