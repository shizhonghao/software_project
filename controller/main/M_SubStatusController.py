# -*- coding: utf-8 -*-
from models.main import SubMatch

class SubStatuController:
    def __init__(self):
        self.messagelist=[]

    def showSub(self):
        self.messagelist=[]
        for x in SubMatch.queue:
            self.messagelist.append(x.getSub())
        print("qqqqqqqq")
        print(self.messagelist)
        return self.messagelist
