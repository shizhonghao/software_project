# -*- coding: utf-8 -*-
from M_database import cursor,db_lock
from datetime import datetime

class Request:

    #更新请求开销
    def costUpdate(self,roomNo,addCost):
        sqlquery = "select max(s_time) from request where room_no = %s group by room_no" % (str(roomNo))
        print(sqlquery)
        db_lock.acquire()
        cursor.execute(sqlquery)
        row = cursor.fetchone()
        db_lock.release()
        if(row == None):
            print("No request from this room")
        else:
            time = row[0]
            sqlquery = "update request set cost = cost + %s where s_time = '%s' and room_no = %s" % (str(addCost),str(time),str(roomNo))
            print(sqlquery)
            db_lock.acquire()
            cursor.execute(sqlquery)
            db_lock.release()


    #结束一个请求
    def endRequest(self,roomNo,temp,windLevel):
        sqlquery = "select max(s_time) from request where room_no = %s group by room_no" % (str(roomNo))
        print(sqlquery)
        db_lock.acquire()
        cursor.execute(sqlquery)
        row = cursor.fetchone()
        db_lock.release()
        if (row == None):
            print("No request from this room")
        else:
            time = row[0]
        endtime = datetime.now()
        sqlquery = "update request set e_time = '%s',e_temp = %s,e_wind_level = %s where room_no = %s and s_time = '%s'" % (str(endtime),str(temp),str(windLevel),str(roomNo),str(time))
        db_lock.acquire()
        cursor.execute(sqlquery)
        db_lock.release()

        #添加新请求
        def newRequest(self,roomNo,temp,windLevel):
            time = datetime.now()
            #终止上个请求
            self.endRequest(roomNo,temp,windLevel)
            sqlquery = "insert into request(room_no,s_temp,s_wind_level,s_time,cost) values(%s,%s,%s,%s,0)" % (str(roomNo),str(temp),str(windLevel),str(time))
            print(sqlquery)
            db_lock.acquire()
            cursor.execute(sqlquery)
            db_lock.release()

    #获得所有房号
    def getRoomNo(self):
        sqlquery = "select distinct room_no from request order by room_no"
        print(sqlquery)
        db_lock.acquire()
        cursor.execute(sqlquery)
        row = cursor.fetchone()
        room = []
        while(row != None):
            room.append(row[0])
            row = cursor.fetchone()
        return room