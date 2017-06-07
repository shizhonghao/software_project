# -*- coding: utf-8 -*-
from models.main import SubMatch

class SubStatuController:
    def __init__(self):
        self.messagelist=[]

    def showSub(self):
        del self.messagelist[:]
        x=0
        SubMatch.setAllservent()
        while x<len(SubMatch.queue):
            self.messagelist.append(SubMatch.queue[x].getSub())
            print(self.messagelist[x])
            x+=1
        print("qqqqqqqq")
        print(self.messagelist)
        return self.messagelist
