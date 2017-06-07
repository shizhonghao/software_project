# -*- coding: utf-8 -*-

from M_database import cursor,db_lock,db
from PyQt5.QtCore import pyqtSignal,QObject

class UserRecord(QObject):
    __tablename__ = 'usr'
    log_sig = pyqtSignal(str, int, str, str, int)

    def Check(self, Room_No, Name, Password):
        print("check:", Room_No, Name, Password)
        Mode = 1  # 这里需要一个获取Mode的函数
        db_lock.acquire()
        sql = "SELECT * FROM " + self.__tablename__ + " WHERE name='%s' and pwd='%s'" % (Name, Password)
        cursor.execute(sql)
        row = cursor.fetchone()
        db_lock.release()
        print(row)
        if row == None:
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
                sql = "INSERT INTO connection values(1,'%s','%s','%s','%s')" % (date, Name, Password, Room_No)
            else:
                print("room exists")
                sql = "ALTER TABLE connection SET is_alive = 1 WHERE room_no='%s' and date='%s'" % (Room_No, date)

    def insertmes(self,name,pwd):
        sql = "insert into usr(name,pwd) value ('%s','%s')" %(name,pwd)

        # 互斥访问，预防并发访问时游标被占用，结果出错
        db_lock.acquire()
        cursor.execute(sql)
        db_lock.release()#释放锁
        db.commit()
        print("插入数据")
        return '登记成功'
