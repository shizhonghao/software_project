# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from client import c
import time

class HeartBeat:
    init_interval = 1000

    def __init__(self,servent):
        #定时器
        self.timer = QTimer()
        self.timer.setInterval(self.init_interval)
        self.timer.start()

        #记下作为心跳操作目标的从机状态类
        self.target = servent
        print('timer set')
        self.timer.timeout.connect(self.state_update)

    def state_update(self):
        #做状态更新
        '''
        2.	温度上报（心跳）（开机时间）
            Temp_Submit
            a.	时间
            Time (yyyy-mm-dd hh:mm:ss) (to be decided later)
            b.	从机编号
            Client_No
            c.	当前室温
            Temp 
        '''
        #当前时间
        current_time=time.localtime(time.time())
        #转化为datetime格式
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',current_time)

        serverNo = self.target.roomNo

        current_temp = self.target.sysT
        print("heart Beat",current_time,serverNo,current_temp)
        c.Temp_Submit(current_temp,serverNo,current_temp)
        #此处应该要更新下刷新频率
        ''''
        self.init_interval +=1000
        self.timer.setInterval(self.init_interval)
        期望是用
        self.timer.setInterval(self.target.freq)之类的
        '''
        #发信