__author__ = '1002097'

import requests
import Weather
import ConfigParser
import json

url = 'http://apis.skplanetx.com/weather/current/hourly?lon=126.8&village=&county=&lat=37.7&city=&version=1'


def headerMake(value) :
    return {'appKey' : value}

def getWeather() :
    config = ConfigParser.RawConfigParser()
    config.read('config.properties')

    ra= requests.get(url,headers=headerMake(config.get('BASIC','weather.key')))
    we = Weather.Weather()

    we.setRawJson(ra.text)
    we.parseWeather()

    print we.getcloud()


getWeather()