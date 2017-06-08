# -*- coding: utf-8 -*-
"""
from M_database import cursor,db_lock
from PyQt5.QtCore import pyqtSignal,QObject

class UsrLogin(QObject):
    log_sig = pyqtSignal(str, int, str, str, int)

    __tablename__ = 'usr'
    def Check(self,Room_No,Name,Password):
        print("check:",Room_No,Name,Password)
        Mode = 1 #这里需要一个获取Mode的函数
        db_lock.acquire()
        sql = "SELECT * FROM " + self.__tablename__ + " WHERE name='%s' and pwd='%s'" % (Name, Password)
        cursor.execute(sql)
        row = cursor.fetchone()
        db_lock.release()
        print(row)
        if row==None:
            print("not connected")
            self.log_sig.emit(Room_No, 0, Name, Password, Mode)
        else:
            print("connected")
            self.log_sig.emit(Room_No, 1, Name, Password, Mode)
            date = 1
            db_lock.acquire()
            sql = "SELECT * FROM connection WHERE room_no='%s' and date='%s'" % (Room_No, date)
            cursor.execute(sql)
            row = cursor.fetchone()
            db_lock.release()
            if row == None:
                print("new room")
                sql = "INSERT INTO connection values(1,'%s','%s','%s','%s')" % (date,Name, Password, Room_No)
            else:
                print("room exists")
                sql = "ALTER TABLE connection SET is_alive = 1 WHERE room_no='%s' and date='%s'" % (Room_No, date)
"""