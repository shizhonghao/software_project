# -*- coding: utf-8 -*-
from client import c
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,QObject
RoomNo = 105
class S_LoginController(QObject):
    _haslogged = pyqtSignal(int, str, str, int)
    def __init__(self):
        super().__init__()
        print("init logincon")
        c._haslogged.connect(self.logged)
        print("connect logincon")

    def Login(self,username,card_id):
        #print('in contro')
        if len(username)==0:
            return False,'输入用户名不应为空'
        if len(card_id)==0:
            return False, '输入身份证号不应为空'

        c.Login(username,card_id,RoomNo)

    def logged(self,Succeed,Name,Password,Mode):
        self._haslogged.emit(Succeed,Name,Password,Mode)