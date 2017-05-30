# -*- coding: utf-8 -*-
from M_database import cursor
from models.Administrator import Administrator
class M_LoginController:
    def Login(self,id,pwd):
        print('in contro')
        res,message = Administrator.select(Administrator(),id,pwd)
        return res,message