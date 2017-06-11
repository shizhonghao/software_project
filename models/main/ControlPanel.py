# -*- coding: utf-8 -*-
from M_database import cursor, db_lock,db
from models.main.Algorithm import currentAlgorithm
from server import server
import datetime,time
from PyQt5.QtCore import QObject

class ControlPanel(QObject):
    curmonth = int(time.strftime("%m", time.localtime()))
    def __init__(self):
        super().__init__()
        self.freq=5  ########默认初始值，过后要改
        server.freq = 5
        self.strat=1 ######默认初始值，策略
        self.connec=[]  #####当前连接房间
        self.statu=0  ########工作模式，0为制冷，1为制热，默认制冷
        self.setStatu(-1)
        self.clearConnec()

##########设置工作状态#######
    def setStatu(self,Model):
        if Model == -1:#自动模式，按月份设定
            if (self.curmonth>=5 and self.curmonth<=10):
                self.statu=0
                server.Model = 0
            else:
                self.statu=1
                server.Model = 1
        else:
            self.statu = Model
            server.Model = Model
        print("now status is ",self.statu)

##########在线从机记录清除（对付上次崩溃）#####
    def clearConnec(self):
        sql = "update connection set is_alive=0"
        db_lock.acquire()
        cursor.execute(sql)
        # 互斥访问，预防并发访问时游标被占用，结果出错
        db.commit()
        db_lock.release()  # 释放锁
##########设置在线从机号#####
    def setConnec(self):
        self.connec=[]
        sql = "select room_no from connection where is_alive=1"
        db_lock.acquire()
        cursor.execute(sql)
        # 互斥访问，预防并发访问时游标被占用，结果出错
        for row in cursor.fetchall():
            #print(row)
            self.connec.append(row[0])
        db_lock.release()  # 释放锁
        #print('共查找出hhhhhhh', cursor.rowcount, '条数据')
        #print(self.connec)
##########根据控制器传的数值设置工作频率#####
    def setFreq(self,freq):
        self.freq=freq
        server.freq = freq
        print(self.freq)
##########根据控制器传的数值设置策略#########
    def setStrat(self,strat):
        self.strat=strat
        currentAlgorithm.changeAlgorithm(strat)

        #print(self.strat)
#########返回信息#########
    def getConnec(self):
        self.setConnec()
        return self.connec

    def getFreq(self):
        return self.freq

    def getStrat(self):
        return self.strat

    def getStatu(self):
        #print("CCCCCCCCCcurentmonth",self.curmonth,)
        #print(datetime.datetime.now().strftime('%Y-%m-%d'))
        return self.statu