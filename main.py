# -*- coding: utf-8 -*-
import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
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


best_match={
    'Aquarius':'You are most compatible with a Sagittarius, Leo, and Gemini. Both Sagittarius and Aquarius are cheerful, energetic, and love adventure and unpredictability. This is a very fortuitous astrology signs love match. Libra and Aquarius both love being around people and share a mutual need for an active social life. This is a match that can make for a wonderfully harmonious marriage. Aquarius and Gemini have the potential to be a match made in heaven.',
    'Pisces':'You are most compatible with a Scorpio, Cancer, and Capricorn. Scorpio and Pisces are likely to feel a strong mutual attraction right away. Scorpio will want to be the leader in the relationship, and Pisces loves to be protected and cared for. Cancer and Pisces are both sensitive signs. This makes for a harmonious match that can easily lead to a happy marriage. Pisces and Capricorn are day & night. his union has excellent potential to become a relationship that is truly delightful and successful.',
    'Aries':'You are most compatible with a Gemini, Sagittarius, and Leo. An Aries-Gemini match will often result in a vibrant relationship that is full of activity and vitality. Sagittarius is another highly energetic sign that can match Aries’s personality. Leo and Aries will ahve to learn to share the spotlight, however, his can be a highly energetic and special union. All 3 are amazing partners in bed.',
    'Taures':'You are most compatible wiht a Cancer, Capricorn, and Pisces. Taurus and Cancer natives share a need for security and an interest in cultivating serious relationship. Capricorn and Taurus also share a mutual and a need for security. Both are interested in forming long term relationships. Taurus and Pisces are similar and different. Both keep each other grounded in a relationship.',
    'Leo':'You are most compatible with a Sagittarius, Aries, and Gemini. Both Sagittarius and Leo are robust, fiery, fun-loving signs that share a mutual love of adventure and freedom. Seeing eye to eye when it comes to important aspects of life, they are built to last. Aries natives and Leoshare a mutual understanding of one another. Their sex life is a key bonding point when it comes to their relationship. Leo and Gemini are signs that approach life with enthusiasm. This is a couple that generally has a wonderful time whenever they are together.',
    "Capricorn":'You are most compatible with a Taures, Pisces, and Virgo. Capricorn and Taurus have a natural understanding of each others approaches to life. This union is one that makes for an excellent marriage. Capricorn and Pisces have differences that are beneficial to the union. They have a very bright future together. Virgo and Capricorn are like two peas in a pod in their approach to life. It is one that stands an excellent chance of long-term success.',
    'Gemini':'You are most compatible with a Libra, Aquarius, and Aries. Gemini and Libra natives understand each other perfectly. Their union will be one that is warm and open, easily standing the test of time. Gemini & Aquarius have a mutual love of interests. These two will enjoy a warm relationship with a strong element of friendship as well. An Aries-Gemini match is an astrology love match that will be full of activity.',
    'Libra':'You are most compatible with an Aquarius, Gemini, and Sagittarius. Both Aquarius and Libra love socializing, talking, and being around people. These two will find it easy to reach a compromise in tough times. Gemini and Libra together make for one of those ideal unions. Libra and Gemini are full of passion when it comes to everything they do. Libra and fiery Sagittarius can be assured that they will never be bored with one another. This union has the makings of a partnership built to last.',
    'Scorpio':'You are most compatible with a Cancer, Capricorn, Pisces. Scorpio and Cancer is a passionate union ideally suited for marriage. Capricorn and Scorpio go together excellently. This will be a union that should blossom into a strong, healthy long-term relationship. Pisces and Scorpio take care of each other. Relationships of all levels are generally very successful with this pairing. ',
    'Virgo':'You are most compatible with a Taures, Cancer, Capricorn.  Both Taurus and Virgo are individuals who tend to be more introverted. This is a wonderful astrology love match that can make for a comfortable, harmonious union. Cancer and Virgo have their differences but are well suited for each other. This a union full of consideration and compassion.',
    'Sagittarius':'You are most compatible with an Aries, Aquarius, and Leo.  Both Aries and Sagittarius natives are active. This is definitely an astrology signs love match built to last. Aquarius and adventurous Sagittarius share many of the same attributes, which makes thier bond strong. Virgo and Capricorn have a tendency to be just like two peas in a pod. They have many similarities that can stand the test of time. ',
    'Cancer':'You are most compatible with a Taures, Scorio, and Virgo. Taurus and Cancer are alike in that they share a common need for security and a sense of permanence . oth signs are sensitive and attentive to their loved ones. Socrpio can provide the protection that a Cancer may need. Each one’s innate personality makes the other feel safe and loved. Virgo-Cancer pairing has an immense capacity for caring. Virgo always speaks from a practical standpoint, while Cancer is more emotive.'
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
       # establishes correct personality report  
        match =""
        if sign == "Aquarius":
           match= best_match['Aquarius']
        elif sign == "Pisces":
            match= best_match['Pisces']
        elif sign == "Aries":
            match= best_match['Aries']
        elif sign == "Taures":
            match= best_match['Taures']
        elif sign == "Leo":
            match= best_match['Leo']
        elif sign == "Gemini":
            match= best_match['Gemini']
        elif sign == "Cancer":
            match= best_match['Cancer']
        elif sign == "Virgo":
            match= best_match['Virgo']
        elif sign == "Libra":
            match= best_match['Libra']
        elif sign == "Scorpio":
            match= best_match['Scorpio']
        elif sign == "Sagittarius":
            match= best_match['Sagittarius']
        elif sign == "Capricorn":
            match= best_match['Capricorn']
        print match
        # establishes best match
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
            'name_key': user_info['name'],
            'match_key':match
        }
        output = result_template.render(the_variable_dict)
        self.response.write(output.encode('utf-8'))
        
app = webapp2.WSGIApplication([
    ('/', Mainpage),
    ('/main2',Mainpage2),
    ('/results',Results),
   # ('/test',test)

], debug=True)

