# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from server import server
import time
from models.main.SubMatch import queue,que_lock#使用中的从机队列
from M_database import cursor,db_lock
#主机心跳包，定时向从机们发送消息
class HeartBeat:
    #初始间隔应该是主机的刷新频率
    init_interval = 1000
    cost_interval = 1000#根据需求，从机房间

    def __init__(self,servent):
        #定时器
        self.timer = QTimer()
        self.timer.setInterval(self.init_interval)
        self.timer.start()

        #记下作为心跳操作目标的从机状态类
        self.target = queue
        print('timer set')
        self.timer.timeout.connect(self.to_servent)

    def to_servent(self):
        #发送的是从机的金额和用量
        #此处应该要更新下刷新频率
        ''''
        
        '''
        #发信
        #先查连接表，取出表中所有的从机（房间号）
        #再查从机记录表，对那些房间号的连接中的记录，取其金钱能量量
        #对他们发送他们现在的金钱