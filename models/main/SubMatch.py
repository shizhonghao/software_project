# -*- coding: utf-8 -*-
from M_database import db_lock,cursor

queue=[]

class SubMatch:
    def __init__(self):
        self.temp = 1
        queue.append(self)

