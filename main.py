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
class Aquarius(webapp2.RedirectHandler): #1
    def get(self):
        aqua_template= the_jinja_env.get_template('')
        self.response.write(aqua_template.render())

class Pisces(webapp2.RedirectHandler): #2
    def get(self):
        pisces_template= the_jinja_env.get_template('')
        self.response.write(pisces_template.render())

class Aries(webapp2.RedirectHandler): #3
    def get(self):
        aries_template= the_jinja_env.get_template('')
        self.response.write(aries_template.render())

class Taures(webapp2.RedirectHandler): #4
    def get(self):
        taures_template= the_jinja_env.get_template('')
        self.response.write(taures_template.render())

class Scorpio(webapp2.RedirectHandler):#5
    def get(self):
        scorpio_template= the_jinja_env.get_template('')
        self.response.write(scorpio_template.render())
        
class Capricorn(webapp2.RedirectHandler): #6
    def get(self):
        capricorn_template= the_jinja_env.get_template('')
        self.response.write(capricorn_template.render())

class Gemini(webapp2.RedirectHandler): #7
    def get(self):
        gemini_template= the_jinja_env.get_template('')
        self.response.write(gemini_template.render())
        
class Libra(webapp2.RedirectHandler): #8
    def get(self):
        libra_template= the_jinja_env.get_template('')
        self.response.write(libra_template.render())

class Leo(webapp2.RedirectHandler): #9
    def get(self):
        leo_template= the_jinja_env.get_template('')
        self.response.write(leo_template.render())
        
class Virgo(webapp2.RedirectHandler): #10
    def get(self):
        virgo_template= the_jinja_env.get_template('')
        self.response.write(virgo_template.render())
        
class Sagittarius(webapp2.RedirectHandler):#11
    def get(self):
        sagittarius_template= the_jinja_env.get_template('')
        self.response.write(sagittarius_template.render())
        
class Cancer(webapp2.RedirectHandler): #12
    def get(self):
        cancer_template= the_jinja_env.get_template('')
        self.response.write(cancer_template.render())
        






# ** END OF ZODIAC PAGES **
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


