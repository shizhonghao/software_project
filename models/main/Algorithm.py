# -*- coding: utf-8 -*-
from models.main.SubMatch import queue,queueMain,que_lock
from models.main.Request import Request
from server import server
from PyQt5.QtCore import *
from operator import itemgetter
import datetime


class Algorithm:
    ##轮转算法用：定时器、时间片大小、起点
    RRtimer = QTimer()
    RR_interval = 1000#轮转时间片
    RR_head = 0
    is_RR = False
    algorithm = 1

    def __init__(self):
        self.RRtimer.timeout.connect(self.RR)
        self.RRtimer.setInterval(self.RR_interval)

    #响应调度算法选中的从机（单个）
    #stop 为true的时候发停风，否则发其要求的风速
    def Serve(self,target,stop):
        roomNo = target[0]
        windLev = target[1]
        target[2] = 1
        if stop == True:
            target[2] = 0
        if windLev ==0:
            target[2] = 0

        #保持实例的一致性（因为直接用实例会有访问冲突问题）
        queueMain.update_blowing(roomNo,target[2])
        print("let roomno %d have wind %d?"%(roomNo,target[2]))
        #向房间发送响应结果
        server.Wind(roomNo,windLev,target[2])

    def RR(self):
        toServe = []
        toStop = []
        que_lock.acquire()
        lenQue = len(queue)
        if lenQue==0:#队列为空的时候，自动停止
            self.stopRR()
        if lenQue<3:#轮转队列小于3
            for one in queue:
                toServe.append([one.RoomNo, one.velocity, one.start_blowing])
        else:#轮转队列大于三
            RR_tail = (self.RR_head + 2)%lenQue
            if RR_tail<self.RR_head: #循环队列
                for i in range(self.RR_head,lenQue):
                    toServe.append([queue[i].RoomNo,queue[i].velocity,queue[i].start_blowing])
                for i in range(0,self.RR_head+1):
                    toServe.append([queue[i].RoomNo,queue[i].velocity,queue[i].start_blowing])
                for i in range(self.RR_head+1, self.RR_head + 1):
                    toStop.append([queue[i].RoomNo,queue[i].velocity,queue[i].start_blowing])
        que_lock.release()
        print("RR out")
        for one in toServe:
            self.Serve(one, False)
        for one in toStop:
            self.Serve(one, True)

    def startRR(self):
        self.RRtimer.start()
        self.is_RR = True
        self.RR_head = 0

    def stopRR(self):
        print("RR STop")
        self.is_RR = False
        self.RRtimer.stop()

    def Priority(self):
        print("高速风优先")
        toServe = []
        toStop = []
        #高速风抢占优先
        que_lock.acquire()
        lenQue = len(queue)
        if lenQue<3:#队列小于3，响应所有
            for one in queue:
                toServe.append([one.RoomNo, one.velocity, one.start_blowing])
        else:
            #找风速最大的三个房间
            #排序一个临时队列（高到低）
            tempque = sorted(queue,key = lambda SubMatch:SubMatch.velocity,reverse=True)
            for i in range(0,3):
                toServe.append([tempque[i].RoomNo, tempque[i].velocity, tempque[i].start_blowing])
            for i in range(3,lenQue+1):
                toStop.append([tempque[i].RoomNo, tempque[i].velocity, tempque[i].start_blowing])
        que_lock.release()
        for one in toServe:
            self.Serve(one, False)
        for one in toStop:
            self.Serve(one, True)

    def FIFS(self):
        print("先来先服务策略")
        # 先来先服务（以该房间最后一次请求的发起时间判断“先”）
        toServe = []
        toStop = []
        que_lock.acquire()
        lenQue = len(queue)
        if lenQue < 3:  # 队列小于3，响应所有
            for one in queue:
                toServe.append([one.RoomNo, one.velocity, one.start_blowing])
        else:
            # 找当前未响应请求中 最后一次 请求时间最早的
            # 一个临时列表,存各个（房间号，最后一次请求时间）元组
            tempque = []
            stopque = []
            for one in queue:
                #该房间最后一次请求的时间
                record = Request.getLatestRequest(one.RoomNo)
                #字符串转datetime
                record = datetime.datetime.strptime(record,'%Y-%m-%d %H:%M:%S')
                if one.velocity == 0:# 目标风速为 0
                    stopque.append(one)
                    continue#则跳过
                #将一个未停风的请求和时间放入列表
                tempque.append([one, record])
            print("time queue as",tempque)
            tempque.sort(key=itemgetter(1))
            for i in range(0,3):
                toServe.append([tempque[i].RoomNo, tempque[i].velocity, tempque[i].start_blowing])
            for one in stopque:
                toStop.append([one[i].RoomNo, one[i].velocity, one[i].start_blowing])
        que_lock.release()
        for one in toServe:
            self.Serve(one, False)
        for one in toStop:
            self.Serve(one, True)

    def changeAlgorithm(self,type):
        print("change current algorithm as %d"%(type))
        self.algorithm = type
        self.activate()

    #对外接口：激活一次调度算法
    def activate(self):
        print("to activate algorithm")
        if self.algorithm == 1:
            if self.is_RR == True:#RR算法不同于其他，不需要反复激活
                return
            else:
                self.is_RR = True#若未激活，则考虑激活（应该在界面上选择算法后改变）
                self.startRR()
        else:
            if self.is_RR == True:#RR算法若已经启动，需要先停下来
                self.stopRR()
                self.is_RR = False
            if self.algorithm == 2:
                self.Priority()
            else:
                self.FIFS()


currentAlgorithm = Algorithm()
server._algorithmActivate.connect(currentAlgorithm.activate)
server._stopRR.connect(currentAlgorithm.stopRR)