# -*- coding: utf-8 -*-
from M_database import cursor, db_lock
from server import server
import datetime,time
cur_model = 0
class ControlPanel:
    curmonth = int(time.strftime("%m", time.localtime()))
    def __init__(self):
        self.freq=50  ########默认初始值，过后要改
        self.strat=1 ######默认初始值，策略
        self.connec=[]  #####当前连接房间
        self.statu=0  ########工作模式，0为制冷，1为制热，默认制冷
        self.setStatu()
        self.setConnec()
##########设置工作状态#######
    def setStatu(self):
        if (self.curmonth>=5 and self.curmonth<=10):
            self.statu=0
            cur_model = 0
        else:
            self.statu=1
            cur_model = 1
##########设置在线从机号#####
    def setConnec(self):
        sql = "select room_no from connection where is_alive=1"
        cursor.execute(sql)
        # 互斥访问，预防并发访问时游标被占用，结果出错
        db_lock.acquire()
        for row in cursor.fetchall():
            print(row)
            self.connec.append(row[0])
        db_lock.release()  # 释放锁
        print('共查找出hhhhhhh', cursor.rowcount, '条数据')
        print(self.connec)
##########根据控制器传的数值设置工作频率#####
    def setFreq(self,freq):
        self.freq=freq
        server.Temp_Submit_Freq(self.freq)
        print(self.freq)
##########根据控制器传的数值设置策略#########
    def setStrat(self,strat):
        self.strat=strat
        print(self.strat)
#########返回信息#########
    def getConnec(self):
        return self.connec

    def getFreq(self):
        return self.freq

    def getStrat(self):
        return self.strat

    def getStatu(self):
        print("CCCCCCCCCcurentmonth",self.curmonth,)
        print(datetime.datetime.now().strftime('%Y-%m-%d'))
        return self.statu