__author__ = '1002097'
#-*- coding: utf-8 -*-


import ConfigParser

class MakeTalkString :

    config=ConfigParser.RawConfigParser()

    def __init__(self):

        self.config.read('config.properties')



    def makeTodayWeather(self,value):
        retValue = self.config.get('TALK','weather.today') % (value)
        return retValue




