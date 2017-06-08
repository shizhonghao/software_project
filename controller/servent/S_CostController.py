# -*- coding: utf-8 -*-
import datetime
from PyQt5.QtCore import *
import time
class S_CostController:
    def __init__(self,servent):
        self.now_time = datetime.datetime.now()
        self.servent = servent
        self.birth_time = datetime.datetime.strptime(servent.loggedOn,'%Y-%m-%d %H:%M:%S')
        self.minitues = 0
        self.hours = 0
        self.secs = 0

    def getTimeCost(self):
        self.now_time = datetime.datetime.now()
        self.minitues , self.secs= divmod((self.now_time - self.birth_time).seconds, 60)
        self.hours, self.minitues = divmod(self.minitues, 60)
        return self.hours,self.minitues,self.secs

    def getEngCost(self):
        print(self.servent.eng_cost)
        return self.servent.eng_cost

    def getMoneyCost(self):
        print(self.servent.money_cost)
        return self.servent.money_cost

