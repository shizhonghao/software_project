# -*- coding: utf-8 -*-
from M_database import cursor, db_lock
from server import server


class ControlPanel:
    def __init__(self):
        self.freq=50  ########默认初始值，过后要改
        self.strat=1 ######默认初始值，策略
        self.connec=[]  #####当前连接房间

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

    def setFreq(self,freq):
        self.freq=freq
        server.Temp_Submit_Freq(self.freq)
        print(self.freq)

    def setStrat(self,strat):
        self.strat=strat
        print(self.strat)

    def getConnec(self):
        return self.connec

    def getFreq(self):
        return self.freq

    def getStrat(self):
        return self.strat