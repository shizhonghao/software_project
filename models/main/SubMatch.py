# -*- coding: utf-8 -*-
from M_database import cursor,db_lock,db
import datetime
import threading
from PyQt5.QtCore import pyqtSignal,QObject
from server import server
que_lock = threading.Lock()
queue=[]
RoomNolist=[]
AliveRoomNolist=[]

class SubMatch:
    def __init__(self,roomNo,name):
        self.ID=name
        self.status=False
        self.switchcnt=0
        self.temp = 0.00
        self.velocity=0
        self.RoomNo=roomNo
        self.isalive=1
        self.cost=0.00
        self.energy=0.00
        que_lock.acquire()
        queue.append(self)
        que_lock.release()
        self.insertItem()

    #########向数据库里插入需要的从机信息############
    def insertItem(self):
        data = self.RoomNo
        sql="select room_no,switch_cnt from servent_stat where room_no=%d and date=CURRENT_DATE " % data
        # 互斥访问，预防并发访问时游标被占用，结果出错
        print("database??",sql)
        db_lock.acquire()
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
        if len(res)==0:
            now=datetime.datetime.now().strftime('%Y-%m-%d')
            sql = "insert into servent_stat values (%d,%d,%f,%d,%f,%f,'%s')"
            data=(self.RoomNo,self.switchcnt,self.temp,self.velocity,self.cost,self.energy,now)
            cursor.execute(sql % data)
            db.commit()
            print("插入数据")
        else:
            #已存在，由于从机被重新初始化，除了开机次数和房间号、日期、消费，剩下字段都更新
            self.switchcnt = res[0][1]
            sql = "update servent_stat set wind_level=%d,temp=%f where room_no='%d' and date=curdate()"\
                  %(self.velocity,self.temp,self.RoomNo)
            cursor.execute(sql)
            db.commit()
            print("更新数据")
        db_lock.release()  # 释放锁

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

    ################根据从机号和当前日期从从机状态表里找到对应的行修改其温度，和实例本身的温度########
    def setTemp(self,temp):
        self.temp = temp
        # 互斥访问，预防并发访问时游标被占用，结果出错
        print("change temp of room %d"%(self.RoomNo))
        db_lock.acquire()
        sql = "update servent_stat set temp=%f where room_no='%d' and date=curdate()" \
              % (self.temp, self.RoomNo)
        cursor.execute(sql)
        db.commit()
        db_lock.release()  # 释放锁
        print("change temp of room %d, complete" % (self.RoomNo))

    ################根据从机号和当前日期从从机状态表里找到对应的行修改其风速，和实例本身的风速########
    def setWindLev(self, velocity):
        self.velocity = velocity
        # 互斥访问，预防并发访问时游标被占用，结果出错
        print("change velocity of room %d" % (self.RoomNo))
        db_lock.acquire()
        sql = "update servent_stat set wind_level=%d where room_no='%d' and date=curdate()" \
              % (self.velocity, self.RoomNo)
        cursor.execute(sql)
        db.commit()
        db_lock.release()  # 释放锁
        print("change velocity of room %d complete" % (self.RoomNo))

  ################根据从机号和当前日期从从机状态表里找到对应的花销消耗，输出二元组列表，不存活的就弄成0########
    def addSwitch_cnt(self):
        self.isalive = 0
        self.cost= 0.00
        self.energy = 0
        sql = "update servent_stat set switch_cnt = switch_cnt+1 where room_no='%d' and date=curdate()" % (self.RoomNo)
        # 互斥访问，预防并发访问时游标被占用，结果出错
        print(sql)
        db_lock.acquire()
        cursor.execute(sql)
        db.commit()
        db_lock.release()  # 释放锁
        print("关机次数更新完成")

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

    def addCost(self,delmonye, deleng):
        self.cost+=delmonye
        self.energy+=deleng
        db_lock.acquire()
        sql = "UPDATE servent_stat SET cost=cost+%f, energy=energy+%f WHERE room_no='%d' and date=curdate()"\
              % (delmonye,deleng,self.RoomNo)
        print(sql)
        cursor.execute(sql)
        db.commit()
        db_lock.release()


class queueMaintance(QObject):
    def __init__(self):
        super().__init__()

    #########从机上行心跳包更新某个从机
    def update_temp(self,roomNo,temp):
        print("to change temp of room%d"%(roomNo))
        que_lock.acquire()
        #找到要修改的从机
        for one in queue:
            if(one.RoomNo == roomNo):
                one.setTemp(temp)
                break
        que_lock.release()

    #温控请求对从机实例的风速修改
    def update_windLev(self,roomNo,windLev):
        que_lock.acquire()
        #找到要修改的从机
        for one in queue:
            if(one.RoomNo == roomNo):
                one.setWindLev(windLev)
                break
        que_lock.release()

    def deleteItem(self,roomno):
        print("将关闭从机%d" % (roomno))
        que_lock.acquire()
        for x in queue:
            if x.RoomNo==roomno:
                x.addSwitch_cnt()
                queue.remove(x)
        que_lock.release()

    #登陆后创建一个新的从机实例
    def newServent(self,roomNo,name):
        print("创建一个新从机")
        SubMatch(roomNo,name)


queueMain = queueMaintance()
server._updateTemp.connect(queueMain.update_temp)
server._newServent.connect(queueMain.newServent)
server._quitServent.connect(queueMain.deleteItem)
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
