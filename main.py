import webapp2
from random import shuffle
import jinja2
import os
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

   



app = webapp2.WSGIApplication([
    ('/', Mainpage)
], debug=True)


