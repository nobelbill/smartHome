__author__ = '1002097'

import json

class Weather() :

    maxTemp=0
    minTemp=0
    avgTemp=0
    humidity=0
    rawJson=''
    cloud=''

    def __init__(self):
        print("init")



    def getMaxTemp(self):
        return self.maxTemp

    def getMinTemp(self):
        return self.minTemp

    def gethumidity(self):
        return self.humidity

    def getcloud(self):
        return self.cloud

    def setRawJson(self,rawData):
        self.rawJson =  rawData

    def parseWeather(self):
        j= json.loads(self.rawJson)
        self.maxTemp=  j['weather']['hourly'][0]['temperature']['tmax']
        self.minTemp=  j['weather']['hourly'][0]['temperature']['tmin']
        self.avgTemp=  j['weather']['hourly'][0]['temperature']['tc']
        self.humidity= j['weather']['hourly'][0]['humidity']
        self.cloud =   j['weather']['hourly'][0]['sky']['name']
        print self.cloud