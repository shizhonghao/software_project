# -*- coding: utf-8 -*-
from models.main.SubMatch import queue,SubMatch
from server import server
import threading
from PyQt5.QtCore import *
from operator import itemgetter

que_lock = threading.Lock()
class Algorithm:
    ##轮转算法用：定时器、时间片大小、起点
    RRtimer = QTimer()
    RR_interval = 1000#轮转时间片
    RR_head = 0
    is_RR = False
    algorithm = 2

    def __init__(self):
        self.RRtimer.setInterval(self.RR_interval)

    #响应调度算法选中的从机（单个）
    #stop 为true的时候发停风，否则发其要求的风速
    def Serve(self,target,stop):
        roomNo = target.RoomNo
        windLev = target.velocity
        if stop == True:
            windLev = 0
        start_Blowing = 0
        if windLev == 0:
            start_Blowing = 0
        #向房间发送响应结果
        server.Wind(roomNo,windLev,start_Blowing)

    def RR(self):
        que_lock.acquire()
        lenQue = len(queue)
        if lenQue<3:#轮转队列小于3
            for one in queue:
                self.Serve(one,False)
        else:#轮转队列大于三
            RR_tail = (self.RR_head + 2)%lenQue
            if RR_tail<self.RR_head: #循环队列
                for i in range(self.RR_head,lenQue):
                    self.Serve(queue[i],False)
                for i in range(0,self.RR_head+1):
                    self.Serve(queue[i],False)
                for i in range(self.RR_head+1, self.RR_head + 1):
                    self.Serve(queue[i], True)
        que_lock.release()

    def startRR(self):
        self.RRtimer.start()
        self.RR_head = 0

    def stopRR(self):
        self.RRtimer.stop()

    def Priority(self):
        #高速风抢占优先
        que_lock.acquire()
        lenQue = len(queue)
        if lenQue<3:#队列小于3，响应所有
            for one in queue:
                self.Serve(one,False)
        else:
            #找风速最大的三个房间
            #排序一个临时队列（高到低）
            tempque = sorted(queue,key = lambda SubMatch:SubMatch.velocity,reverse=True)
            for i in range(0,3):
                self.Serve(tempque[i],False)
            for i in range(3,lenQue+1):
                self.Serve(tempque[i],True)
        que_lock.release()

    def FIFS(self):
        # 高速风抢占优先
        que_lock.acquire()
        lenQue = len(queue)
        if lenQue < 3:  # 队列小于3，响应所有
            for one in queue:
                self.Serve(one,False)
        else:
            # 找当前未响应请求中 最后一次 请求时间最早的
            # 一个临时列表,存各个（房间号，最后一次请求时间）元组
            tempque = []
            stopque = []
            for one in queue:
                #from request import ???
                #records = "select * from request where s_time在今天内   order by s_time"
                #if records == None:
                #   continue
                #else:
                #   lastAt = len(records)
                #   record = records[lastAt]
                record=[]
                if record[6] == 0:# 目标风速为 0
                    stopque.append(one)
                    continue#则跳过
                #将一个未停风的请求和时间放入列表
                tempque.append([one, record[1]])
            #
            tempque.sort(key=itemgetter(1))
            for i in range(0,3):
                self.Serve(tempque[i][0],False)
            for one in stopque:
                self.Serve(one,True)
        que_lock.release()

    def changeAlgorithm(self,type):
        self.algorithm = type

    #对外接口：激活一次调度算法
    def activate(self):
        if self.algorithm == 1:
            if self.is_RR == True:#RR算法不同于其他，不需要反复激活
                continue
            else:
                self.is_RR = True


currentAlgorithm = Algorithm()