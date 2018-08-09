import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
#from requests_toolbelt.adapters import appengine
#appengine.monkeypatch()
import sdk
import re

userID = "602635";
apiKey = "1d6bc9e59f87b63b70bc675c4269e173";

clientInstance = sdk.VRClient(userID, apiKey)

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

zodiac_info={
    '':"",
    '':""
}

user_info={
    'name':"",
    'sign':"",
    'url':"",
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
        main_template2= the_jinja_env.get_template('templates/main_page2.html')
        name = self.request.get('user_name')
        user_info['name']=name
        self.response.write(main_template2.render(user_info))

class Mainpage2(webapp2.RedirectHandler):
    def get(self):
        main_template= the_jinja_env.get_template('templates/main_page2.html')
        self.response.write(main_template.render(user_info))
    def post(self):
        main_template= the_jinja_env.get_template('templates/main_page2.html')

        self.response.write(main_template.render())   

class Results(webapp2.RedirectHandler):
    def post(self):
        print "=========Results (post)========="
        result_template= the_jinja_env.get_template('templates/results.html')
        sign = self.request.get('sign')
        if sign == "Aquarius":
            data['month']=4
        elif sign =="Pisces":
            data['month']=5
        elif sign =="Aries":
            data['month']=6
        elif sign =="Taures":
            data['month']=7
        elif sign =="Gemini":
            data['month']=8
        elif sign =="Cancer":
            data['month']=9
        elif sign =="Leo":
            data['month']=10
        elif sign =="Virgo":
            data['month']=11
        elif sign =="Libra":
            data['month']=12
        elif sign =="Scorpio":
            data['month']=1
        elif sign =="Sagittarius":
            data['month']=2
        elif sign =="Capricorn":
            data['month']=3
        resource = "general_ascendant_report/tropical" # sets destination of info to extract
        ritesh = sdk.VRClient(userID,apiKey)  # destroys paywall
        zodiac_info = ritesh.call(resource, data['date'], data['month'], data['year'], data['hour'], data['minute'], data['latitude'], data['longitude'], data['timezone']);
        # sets the information to a dictionary/variable
        ascendant = zodiac_info['ascendant']
        report= zodiac_info['report']
        # stores the info from URL into a variable
        the_variable_dict = {
            'report_key': report.decode('utf-8'),
            'sign_key': sign,
            'ascendant_key':ascendant,
            'background_url_key': zodiac_backgrounds[sign],
            'name_key': user_info['name']
        }
        output = result_template.render(the_variable_dict)
        self.response.write(output.encode('utf-8'))

app = webapp2.WSGIApplication([
    ('/', Mainpage),
    ('/main2',Mainpage2),
    ('/results',Results),
   # ('/test',test)

], debug=True)

