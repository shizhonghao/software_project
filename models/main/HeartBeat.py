# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from server import server
import time
from models.main.SubMatch import queue,que_lock#使用中的从机队列
from M_database import cursor,db_lock
from models.main.Request import Request

#主机心跳包，定时向从机们发送消息
class HeartBeat:
    #初始间隔应该是主机的刷新频率
    init_interval = 3000
    cost_interval = 1000#根据需求，从机房间

    def __init__(self,freq):
        #定时器
        self.timer = QTimer()
        self.cost_interval=freq
        self.timer.setInterval(self.init_interval)
        self.timer.start()

        #记下作为心跳操作目标的从机状态类
        self.target = queue
        print('timer set')
        self.timer.timeout.connect(self.to_servent)

    def to_servent(self):
        toSend=[]
        que_lock.acquire()
        for one in queue:
            #server.Fare_Info(one.RoomNo,one.cost,one.energy)
            #print("to change freq of servent as %d" %(self.cost_interval))
            #临时的计价
            w = 1.0*self.init_interval/60000.0
            if one.velocity*one.start_blowing == 3:
                one.addCost(1.3*5.0*w,1.3*w)
                Request.costUpdate(Request(), one.RoomNo, 1.3*5.0*w)
            elif one.velocity*one.start_blowing == 2:
                one.addCost(5.0*w,1.0*w)
                Request.costUpdate(Request(), one.RoomNo, 1.0 * 5.0 * w)
            elif one.velocity*one.start_blowing == 1:
                one.addCost(0.8*5.0*w,1.0*w)
                Request.costUpdate(Request(), one.RoomNo, 0.8 * 5.0 * w)
            toSend.append([one.RoomNo,one.cost,one.energy])
        que_lock.release()

        for oneroom in toSend:
            server.Fare_Info(oneroom[0],oneroom[1],oneroom[2])
            server.Temp_Submit_Freq(oneroom[0],self.cost_interval)


    def changeSubmintFreq(self,freq):
        self.cost_interval = freq
        self.to_servent()