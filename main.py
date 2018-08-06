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
        main_template= the_jinja_env.get_template('tempaltes/main_page.html')
        self.response.write(main_template.render())
        


class Zodiac_info(webapp2.RedirectHandler):
    def get(self):
        info_template= the_jinja_env.get_template('')
        self.response.write(info_template.render())
#needs horoscope api        
        
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


