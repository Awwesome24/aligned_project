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
    
    
    
    
class Mainpage(webapp2.RedirectHandler):
    def get(self):
        main_template= the_jinja_env.get_template('templates/main_page.html')
        self.response.write(main_template.render())
        
#horoscope api for all zodiacs      

# ** ZODIAC HANDLERS **
class Aquarius(webapp2.RedirectHandler):
    def get(self):
        aqua_template= the_jinja_env.get_template('')
        self.response.write(aqua_template.render())

class Pisces(webapp2.RedirectHandler):
    def get(self):
        pisces_template= the_jinja_env.get_template('')
        self.response.write(pisces_template.render())

class Aries(webapp2.RedirectHandler):
    def get(self):
        aries_template= the_jinja_env.get_template('')
        self.response.write(aries_template.render())

class Taures(webapp2.RedirectHandler):
    def get(self):
        taures_template= the_jinja_env.get_template('')
        self.response.write(taures_template.render())




class lsf_page(webapp2.RedirectHandler):
    def get(self):
        lsf_template= the_jinja_env.get_template('')
        self.response.write(lsf_template.render())

class api_page(webapp2.RedirectHandler):
    def get(self):
        api_template= the_jinja_env.get_template('')
        self.response.write(api_template.render())
# requires an API


app = webapp2.WSGIApplication([
    ('/', Mainpage)
], debug=True)


