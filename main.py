import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
#from requests_toolbelt.adapters import appengine
#appengine.monkeypatch()
import sdk

userID = "602635";
apiKey = "1d6bc9e59f87b63b70bc675c4269e173";

clientInstance = sdk.VRClient(userID, apiKey)

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

zodiac_info={
    'ascendant':"",
    'report':""
}

user_info={
    'name':"",
    'sign':"",
    'url':"",
    'gender':"",
    'month':"",
    'day':"",
    'year':""
    }
    
data = {
    'date': 30,
    'month': 10,
    'year': 2012,
    'hour': 0,
    'minute': 0,
    'latitude': 0,
    'longitude': 0,
    'timezone': 0
    }    

zodiac_backgrounds={
    'Aquarius':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-aquarius-and-horoscope-wheel-on-the-dark-blue-background_by6wer0hg_thumbnail-full01.png',
    'Pisces':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-pisces-and-horoscope-wheel-on-the-dark-blue-background_s3zb_kirz_thumbnail-full01.png',
    'Aries':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-aries-and-horoscope-wheel-on-the-dark-blue-background_snzz6l_prz_thumbnail-full01.png',
    'Taures':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-taurus-and-horoscope-wheel-on-the-dark-blue-background_h3d4r5khm_thumbnail-full01.png',
    'Leo':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-leo-and-horoscope-wheel-on-the-dark-blue-background_shfn95ybg_thumbnail-full01.png',
    'Capricorn':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-capricorn-and-horoscope-wheel-on-the-dark-blue-background_s3eo5vjobf_thumbnail-full01.png',
    'Gemini':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-gemini-and-horoscope-wheel-on-the-dark-blue-background_h3xhlc_abf_thumbnail-full01.png',
    'Libra':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-libra-and-horoscope-wheel-on-the-dark-blue-background_htrywarsm_thumbnail-full01.png',
    'Scorpio':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-scorpio-and-horoscope-wheel-on-the-dark-blue-background_hhghwyibg_thumbnail-full01.png',
    'Virgo':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-virgo-and-horoscope-wheel-on-the-dark-blue-background_bntos9trg_thumbnail-full01.png',
    'Sagittarius':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-sagittarius-and-horoscope-wheel-on-the-dark-blue-background_htvwq0rbm_thumbnail-full01.png',
    'Cancer':'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/BKpZoQ4viqlda90c/videoblocks-zodiac-sign-cancer-and-horoscope-wheel-on-the-dark-blue-background_s3wxt2uphf_thumbnail-full01.png'
}


    
class Mainpage(webapp2.RedirectHandler):
    def get(self):
        main_template= the_jinja_env.get_template('templates/main_page.html')
        self.response.write(main_template.render())
    def post(self):
        main_template= the_jinja_env.get_template('templates/main_page2.html')
        name = self.request.get('user_name')
        month = self.request.get('user_month')
        day= self.request.get('user_day')
        year= self.request.get('user_year')
        gender=self.request.get('user_gender')
        user_info['name']=name
        user_info['month']=month
        user_info['day']=day
        user_info['year']=year
        user_info['gender']=gender
        print(name)
        print(month)
        print(day)
        print(year)
        print(gender)
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

class results(webapp2.RedirectHandler):
    def get(self):
        result_template= the_jinja_env.get_template('templates/results.html')
        self.response.write(result_template.render(user_info))


class test(webapp2.RedirectHandler):
    def get(self):

        resource = "general_ascendant_report/tropical"
    
        # instantiate VedicRishiClient class
        ritesh = sdk.VRClient(userID,apiKey)
        
        #print("Ascendant: ")
        # call horoscope apis
        zodiac_info = ritesh.call(resource, data['date'], data['month'], data['year'], data['hour'], data['minute'], data['latitude'], data['longitude'], data['timezone']);
        # print(user_info['ascendant'])
        # print(user_info['report'])
        self.response.write(zodiac_info['ascendant'])
        self.response.write(zodiac_info['report'])
        self.response.write(user_info['name'])
        #self.response.write(responseData)

#horoscope api for all zodiacs      

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
    ('/results',results),
    ('/test',test)
], debug=True)

