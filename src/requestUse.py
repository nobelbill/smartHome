__author__ = '1002097'

import requests
import Weather
import ConfigParser

class RequestUse :

    def headerMake(self,value) :
        return {'appKey' : value}

    def getWeather(self) :
        config = ConfigParser.RawConfigParser()
        config.read('config.properties')
        url = config.get('BASIC','weather.url')
        ra= requests.get(url,headers= self.headerMake(config.get('BASIC','weather.key')))
        we = Weather.Weather()

        we.setRawJson(ra.text)
        we.parseWeather()

        print we.getcloud()

ru = RequestUse()
ru.getWeather()
