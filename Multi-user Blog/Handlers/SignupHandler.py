
import os
import jinja2
import webapp2
from Handlers.MainHandler import MainHandler
from Handlers.LoginHandler import LoginHandler
import utility
from Entities.entities import *
import logging

class SingupHandler(MainHandler):
    def get(self):
        self.render("signup.html")

    def done(self,params):
        logging.info(params)
        u = User.by_name(params['username'])
        logging.info(u)
        if u:
            error = "User already exists!"
            self.render("login.html",error=error)
        else:
            u = User.register(params['username'], params['password'], params['email'])
            u.put()
            self.login(u)
            self.redirect("/blog/newpost")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify_pass = self.request.get('verify_password')
        email = self.request.get('email')

        params = dict(username=username,password=password,
                      email=email)
        logging.info(params)
        #validate and redirect accordingly
        if not utility.valid_username(username):
            params['error'] = "Invalid username!!"
            self.render("signup.html",**params)

        elif not utility.valid_password(password):
            params['error']="Invalid password!!"
            self.render("signup.html",**params)

        elif password != verify_pass:
            params['error']="Passwords did not match!"
            self.render("signup.html",**params)

        elif not utility.valid_email(email):
            params['error']="Please enter valid email address!"
            self.render("signup.html",**params)
        else:
            self.render("welcome.html",username=username)

        self.done(params)