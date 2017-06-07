# -*- coding: utf-8 -*-
from M_database import cursor,db_lock,db
import datetime
import threading
que_lock = threading.Lock()
queue=[]
RoomNolist=[]
AliveRoomNolist=[]

class SubMatch:
    def __init__(self):
        self.ID=""
        self.status=False
        self.switchcnt=0
        self.temp=0.00
        self.velocity=0
        self.RoomNo=0
        self.isalive=0
        self.cost=0.00
        self.energy=0.00
        que_lock.acquire()
        queue.append(self)
        que_lock.release()
        self.insertItem()

    #########向数据库里插入需要的从机信息############
    def insertItem(self):
        sql="select room_no,date from servent_stat where room_no='%d' and date=curdate()"
        data = self.RoomNo
        # 互斥访问，预防并发访问时游标被占用，结果出错
        db_lock.acquire()
        cursor.execute(sql % data)
        if len(cursor.fetchall())==0:
            now=datetime.datetime.now().strftime('%Y-%m-%d')
            sql = "insert into servent_stat values (%d,%d,%f,%d,%f,%f,'%s')"
            data=(self.RoomNo,self.switchcnt,self.temp,self.velocity,self.cost,self.energy,now)
            # 互斥访问，预防并发访问时游标被占用，结果出错
            db_lock.acquire()
            cursor.execute(sql % data)
            db_lock.release()  # 释放锁
            db.commit()
            print("插入数据")
        db_lock.release()  # 释放锁

    def setRoomno(self,roomno):
        self.RoomNo=roomno
    ###########根据从机号从connection表里找到对应的用户名和工作状态，输出二元组列表#########
    def setID(self):
        sql = "SELECT name,is_alive FROM connection where room_no='%d'"
        data=self.RoomNo
        # 互斥访问，预防并发访问时游标被占用，结果出错
        db_lock.acquire()
        cursor.execute(sql % data)
        for row in cursor.fetchall():
            self.ID=row[0]
            self.isalive=row[1]
            print(row)
        db_lock.release()  # 释放锁
    ##########是否存活。。加一个判断？#######
    def alive(self):
        if self.isalive==0:
            return False
        else:
            return True
    ################根据从机号和当前日期从从机状态表里找到对应的实时风速和温度，输出二元组列表，不存活的就弄成0########
    def setOther(self):
        if self.isalive==0:
            self.temp=0.00
            self.velocity=0
        else:
            sql = "SELECT temp,wind_level FROM servent_stat where room_no='%d' and date=curdate()"
            data = self.RoomNo
            # 互斥访问，预防并发访问时游标被占用，结果出错
            db_lock.acquire()
            cursor.execute(sql % data)
            for row in cursor.fetchall():
                self.temp = row[0]
                self.velocity = row[1]
                print(row)
            db_lock.release()  # 释放锁

  ################根据从机号和当前日期从从机状态表里找到对应的花销消耗，输出二元组列表，不存活的就弄成0########
    def setCost(self):
        if self.isalive == 0:
            self.cost= 0.00
            self.energy = 0
        else:
            sql = "SELECT cost,energy FROM servent_stat where room_no='%d' and date=curdate()"
            data = self.RoomNo
            # 互斥访问，预防并发访问时游标被占用，结果出错
            db_lock.acquire()
            cursor.execute(sql % data)
            for row in cursor.fetchall():
                self.cost = row[0]
                self.energy = row[1]
                print(row)
            db_lock.release()  # 释放锁
    ############监视界面需要的信息，输出五元组列表#######
    def getSub(self):
        list=[self.RoomNo,self.ID,self.isalive,self.temp,self.velocity]
        print(list)
        return list
    ##########从机请求需要的钱和能量，输出二元组列表######
    def getCost(self):
        list=[self.cost,self.energy]
        print(list)
        return list

    def deleteItem(self,roomno):
        que_lock.acquire()
        for x in queue:
            if x.RoomNo==roomno:
                queue.remove(x)
        que_lock.release
''''
#######从数据表找到从机号######
def getRoomNo():
    del RoomNolist[:]
    sql = "SELECT distinct room_no FROM servent_stat"
    # 互斥访问，预防并发访问时游标被占用，结果出错
    db_lock.acquire()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
        RoomNolist.append(row[0])
    db_lock.release()  # 释放锁
    print('共查找出', cursor.rowcount, '条数据')
    print(RoomNolist)
#######从机队列#####
def setAllservent():
    del queue[:]
    x=0
    getRoomNo()
    print(RoomNolist)
    while x<len(RoomNolist):
        sub=SubMatch()
        sub.setRoomno(RoomNolist[x])
        sub.setID()
        sub.setOther()
        sub.setCost()
        print(sub.getSub())
        print(queue[x].getSub())
        x+=1

#######在线房间号######
def getAliveRoomNo(self):
    del AliveRoomNolist[:]
    sql = "select room_no from connection where is_alive=1"
    cursor.execute(sql)
    # 互斥访问，预防并发访问时游标被占用，结果出错
    db_lock.acquire()
    for row in cursor.fetchall():
        print(row)
        AliveRoomNolist.append(row[0])
    db_lock.release()  # 释放锁
    print('共查找出hhhhhhh', cursor.rowcount, '条数据')
    print(AliveRoomNolist)
#######在线从机？过后改###
def setAliveservent():
    del queue[:]
    x=0
    getAliveRoomNo()
    print(AliveRoomNolist)
    while x<len(AliveRoomNolist):
        sub=SubMatch()
        sub.setRoomno(AliveRoomNolist[x])
        sub.setID()
        sub.setOther()
        sub.setCost()
        print(sub.getSub())
        print(queue[x].getSub())
        x+=1
        '''''
