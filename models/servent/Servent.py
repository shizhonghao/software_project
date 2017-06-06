# -*- coding: utf-8 -*-

from  datetime  import  *
from S_DBFacade import db_lock,cursor,db

myroom = object

class S_servent :
    def __init__(self,U,P,M):
        self.roomNo = 826
        self.targetT = 27
        self.targetW = 1
        self.sysT = 30
        self.sysW = 1
        self.sysModel = M
        self.loggedOn = datetime.strptime("2017-06-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        self.eng_cost = 0.00
        self.money_cost = 0.00
        self.start_blowing = 1

        self.usr = U
        self.pwd = P
        self.insert_deal(self.roomNo, self.loggedOn, self.usr, self.pwd, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.eng_cost, self.money_cost)
        print("out")

    #更新修改当前的系统信息
    def update_sys(self,T,W,M):
        self.targetT = T
        self.targetW = W
        self.sysModel = M
        self.updatesys_deal(self.roomNo, self.loggedOn, T, W, M)               #数据库同步修改

    def update_cost(self,EC,MC):
        self.eng_cost = EC
        self.money_cost = MC
        self.updatecost_deal(self.roomNo, self.loggedOn, EC, MC)                #数据库同步修改

    def update_rt(self,sT): #实时温度心跳包
        self.sysT=sT
        self.updatert_deal(self.roomNo, self.loggedOn, sT)

    def update_rw(self,sW):
        self.sysW=sW
        self.updaterw_deal(self.roomNo, self.loggedOn, sW)



    def ret_current_state(self):
        return self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing
        #这个地方返回的东西还要再修改一下

    def insert_dbinfo(self):
        self.insert_deal()

    def insert_deal(self,roomNo, loggedOn, usr, pwd, targetT, targetW, sysT, sysW, sysModel, eng_cost, money_cost):
        sql = "insert into clientinfo values (%d, '%s', '%s', '%s', %d, %d, %d, %d, %d, %f, %f)" % \
              (roomNo, loggedOn, usr, pwd, targetT, targetW, sysT, sysW, sysModel, eng_cost, money_cost)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()

    def updatecost_deal(self,roomNo, loggedOn, EC, MC):
        sql = "update clientinfo set eng_cost = %f, money_cost = %f where roomNo = %d and loggedOn = %s" % (
        EC, MC, roomNo, loggedOn)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()

    def updatesys_deal(self,roomNo, loggedOn, T, W, M):
        sql = "update clientinfo set targetT = %d, targetW = %d, sysModel = %d where roomNo = %d and loggedOn = %s" % (
        T, W, M, roomNo, loggedOn)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()

    def updatert_deal(roomNo, loggedOn, T):
        sql = "update clientinfo set sysT=%d where where roomNo = %d and loggedOn = %s" % (T, roomNo, loggedOn)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()

    def updaterw_deal(self,roomNo, loggedOn, W):
        sql = "update clientinfo set sysW=%d where where roomNo = %d and loggedOn = %s" % (W, roomNo, loggedOn)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()

