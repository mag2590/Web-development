#All the helper functions necessary for the project will go here

import re
import random
import hashlib
import jinja2
import os
from string import letters
import hmac

template_dir = os.path.join(os.path.dirname(__file__),'templates')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def render_str(template, **params):
    t = JINJA_ENVIRONMENT.get_template(template)
    return t.render(params)

def valid_username(username):
    name_regex = re.compile(r"[a-zA-Z0-9_-]{3,20}$")
    return username and name_regex.match(username)

def valid_password(password):
    pass_regex = re.compile(r"^.{3,20}$")
    return password and pass_regex.match(password)

def valid_email(email):
    email_regex = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
    return not email or email_regex.match(email)


#Code for password hashing and hmac with secret

def make_salt(size=5):
    return ''.join(random.choice(letters) for x in xrange(size))

def make_pw_hash(username, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(username+pw+salt).hexdigest()
    return '%s,%s' %(salt,h)

def validate_pw(username, password, hash):
    salt = hash.split(',')[0]
    #h  = hash.split(',')[1]
    return hash == make_pw_hash(username, pw, salt)

def make_secure_key(key):
    return '%s|%s' % (key,hmac.new(SECRET, key).hexdigest())

def check_secure_key(secure_key):
    key = secure_key.split('|')[0]
    if secure_key == make_secure_key(key):
        return key
    else:
        return None