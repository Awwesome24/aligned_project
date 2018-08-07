import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


user_info={
    'name':"",
    'sign':"",
    'url':""
    }

zodiac_backgrounds={
    'aquarius':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-aquarius-and-horoscope-wheel-on-the-dark-blue-background_by6wer0hg_thumbnail-full01.png',
    'pisces':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-pisces-and-horoscope-wheel-on-the-dark-blue-background_s3zb_kirz_thumbnail-full01.png',
    'aries':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-aries-and-horoscope-wheel-on-the-dark-blue-background_snzz6l_prz_thumbnail-full01.png',
    'taures':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-taurus-and-horoscope-wheel-on-the-dark-blue-background_h3d4r5khm_thumbnail-full01.png',
    'leo':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-leo-and-horoscope-wheel-on-the-dark-blue-background_shfn95ybg_thumbnail-full01.png',
    'capricorn':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-capricorn-and-horoscope-wheel-on-the-dark-blue-background_s3eo5vjobf_thumbnail-full01.png',
    'gemini':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-gemini-and-horoscope-wheel-on-the-dark-blue-background_h3xhlc_abf_thumbnail-full01.png',
    'libra':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-libra-and-horoscope-wheel-on-the-dark-blue-background_htrywarsm_thumbnail-full01.png',
    'scorpio':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-scorpio-and-horoscope-wheel-on-the-dark-blue-background_hhghwyibg_thumbnail-full01.png',
    'virgo':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-virgo-and-horoscope-wheel-on-the-dark-blue-background_bntos9trg_thumbnail-full01.png',
    'sagittarius':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-sagittarius-and-horoscope-wheel-on-the-dark-blue-background_htvwq0rbm_thumbnail-full01.png',
    'cancer':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-cancer-and-horoscope-wheel-on-the-dark-blue-background_s3wxt2uphf_thumbnail-full01.png'
}
    
class Mainpage(webapp2.RedirectHandler):
    def get(self):
        main_template= the_jinja_env.get_template('templates/main_page.html')
        self.response.write(main_template.render())
    
    def post(self):
        main_template= the_jinja_env.get_template('templates/main_page2.html')
        name = self.request.get('user_name')
        print(name)
        user_info['name']=name
        self.response.write(main_template.render(user_info))
        

class Mainpage2(webapp2.RedirectHandler):
    def get(self):
        main_template= the_jinja_env.get_template('templates/main_page2.html')
        self.response.write(main_template.render(user_info))
    def post(self):
        main_template= the_jinja_env.get_template('templates/results.html')
        sign = self.request.get('sign')
        user_info['sign']= sign
        user_info['url']= zodiac_backgrounds[sign]
        self.response.write(main_template.render(user_info))    


#horoscope api for all zodiacs      

# ** ZODIAC HANDLERS **
# Jamiel's
class Aquarius(webapp2.RedirectHandler): #1
    def get(self):
        aqua_template= the_jinja_env.get_template('templates/aquarius.html')
        self.response.write(aqua_template.render(user_info))


class Pisces(webapp2.RedirectHandler): #2
    def get(self):
        pisces_template= the_jinja_env.get_template('templates/pisces.html')
        self.response.write(pisces_template.render())

class Aries(webapp2.RedirectHandler): #3
    def get(self):
        aries_template= the_jinja_env.get_template('templates/aries.html')
        self.response.write(aries_template.render())

class Taures(webapp2.RedirectHandler): #4
    def get(self):
        taures_template= the_jinja_env.get_template('templates/taures.html')
        self.response.write(taures_template.render())

#Joel's
class Leo(webapp2.RedirectHandler):#5
    def get(self):
        leo_template= the_jinja_env.get_template('templates/leo.html')
        self.response.write(leo_template.render())
        
class Capricorn(webapp2.RedirectHandler): #6
    def get(self):
        capricorn_template= the_jinja_env.get_template('templates/capricorn.html')
        self.response.write(capricorn_template.render())

class Gemini(webapp2.RedirectHandler): #7
    def get(self):
        gemini_template= the_jinja_env.get_template('templates/gemini.html')
        self.response.write(gemini_template.render())
        
class Libra(webapp2.RedirectHandler): #8
    def get(self):
        libra_template= the_jinja_env.get_template('templates/libra.html')
        self.response.write(libra_template.render())



#Eric's
class Scorpio(webapp2.RedirectHandler): #9
    def get(self):
        scorpio_template= the_jinja_env.get_template('templates/scorpio.html')
        self.response.write(scorpio_template.render())
        
class Virgo(webapp2.RedirectHandler): #10
    def get(self):
        virgo_template= the_jinja_env.get_template('templates/virgo.html')
        self.response.write(virgo_template.render())
        
class Sagittarius(webapp2.RedirectHandler):#11
    def get(self):
        sagittarius_template= the_jinja_env.get_template('templates/sagittarius.html')
        self.response.write(sagittarius_template.render())
        
class Cancer(webapp2.RedirectHandler): #12
    def get(self):
        cancer_template= the_jinja_env.get_template('templates/cancer.html')
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
    ('/', Mainpage),
    ('/main2',Mainpage2),
    ('/aquarius',Aquarius),
    ('/aries',Aries),
    ('/cancer',Cancer),
    ('/capricorn',Capricorn),
    ('/gemini',Gemini),
    ('/leo',Leo),
    ('/libra',Libra),
    ('/pisces',Pisces),
    ('/sagittarius',Sagittarius),
    ('/scorpio',Scorpio),
    ('/taures',Taures),
    ('/virgo', Virgo)
], debug=True)

# NAME FIRST STORE IT AS A VARIABLE AND THEN DO HREF's FOR HTML
