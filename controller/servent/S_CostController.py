# -*- coding: utf-8 -*-
import datetime
from PyQt5.QtCore import *
import time
class S_CostController:
    def __init__(self):
        self.birth_time = datetime.datetime.now()
        self.now_time = datetime.datetime.now()
        self.minitues = 0
        self.hours = 0
        self.secs = 0

    def getTimeCost(self):
        self.now_time = datetime.datetime.now()
        self.minitues , self.secs= divmod((self.now_time - self.birth_time).seconds, 60)
        self.hours, self.minitues = divmod(self.minitues, 60)

    def getCost(self):
        self.getTimeCost()
