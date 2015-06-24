__author__ = '1002097'
#-*- coding: utf-8 -*-
import requests
import Weather
import ConfigParser
import sys
import MakeTalkString

class RequestUse :

    config = ConfigParser.RawConfigParser()
    def __init__(self):

        self.config.read('config.properties')

    def headerMake(self,value) :
        return {'appKey' : value}

    def getWeather(self) :

        url = self.config.get('BASIC','weather.url')
        ra= requests.get(url,headers= self.headerMake(self.config.get('BASIC','weather.key')))
        we = Weather.Weather()

        we.setRawJson(ra.text)
        we.parseWeather()

    def getMp3File(self,value):
        headers = {'User-Agent': 'Mozilla/5.0'}
        ttsUrl= self.config.get('TTS','base.url') + value
        response = requests.get(ttsUrl,headers=headers)
        f = open('workfile.mp3', 'w+b')
        f.write(response.content)
        f.close()




reload(sys)
sys.setdefaultencoding('utf-8')
ru = RequestUse()
mts=MakeTalkString.MakeTalkString()

ru.getMp3File( str((mts.makeTodayWeather(1))))