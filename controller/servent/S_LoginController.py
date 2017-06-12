# -*- coding: utf-8 -*-
from client import c
from PyQt5.QtWidgets import *
import re
from PyQt5.QtCore import pyqtSignal,QObject

class S_LoginController(QObject):
    _haslogged = pyqtSignal(int,int, str, str, int)
    _inputFailed = pyqtSignal(bool,str)
    roomNo = 3
    def __init__(self):
        super().__init__()
        c._haslogged.connect(self.logged)

    def Login(self,roomNo,username,card_id):
        #print('in contro')
        usrnameMatch = re.match(r'.*[\'\"\\].*', username, re.S | re.I)
        print(usrnameMatch)

        if len(roomNo)==0:
            self._inputFailed.emit(False,'输入房间号不应为空')
            return
        elif roomNo.isdigit()==False:
            self._inputFailed.emit(False, '输入房间号必须为纯数字')
            return

        if len(username)==0:
            self._inputFailed.emit(False,'输入用户名不应为空')
            return
        elif usrnameMatch!=None:
            self._inputFailed.emit(False, '输入用户名含有非法字符(\',\",\\)')
            return

        if len(card_id)==0:
            self._inputFailed.emit(False, '输入身份证号不应为空')
            return
        elif card_id.isdigit()==False:
            self._inputFailed.emit(False, '输入身份证号必须为纯数字')
            return

        self.roomNo = int(roomNo)
        c.Login(username,card_id,roomNo)

    def logged(self,Succeed,Name,Password,Mode):
        self._haslogged.emit(self.roomNo,Succeed,Name,Password,Mode)