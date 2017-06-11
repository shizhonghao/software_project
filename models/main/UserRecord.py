# -*- coding: utf-8 -*-

from M_database import cursor,db_lock,db
from PyQt5.QtCore import pyqtSignal,QObject
from datetime import datetime

class UserRecord(QObject):
    __tablename__ = 'usr'
    log_sig = pyqtSignal(str, int, str, str)

    def Check(self, Room_No, Name, Password):
        print("check:", Room_No, Name, Password)
        db_lock.acquire()
        sql = "SELECT * FROM " + self.__tablename__ + " WHERE name='%s' and pwd='%s'" % (Name, Password)
        cursor.execute(sql)
        row = cursor.fetchone()
        db_lock.release()
        print(row)
        if row == None:
            print("not connected")
            self.log_sig.emit(Room_No, 0, Name, Password)
            #return False
        else:
            print("connected")
            self.log_sig.emit(Room_No, 1, Name, Password)
            date = datetime.now()
            start = datetime(date.year, date.month, date.day, 0, 0, 0)
            end = datetime(date.year, date.month, date.day, 23, 59, 59)
            db_lock.acquire()
            sql = "SELECT * FROM connection WHERE room_no=%d and login_time between '%s' and '%s'" % (int(Room_No), start, end)
            cursor.execute(sql)
            row = cursor.fetchone()
            db_lock.release()
            if row == None:
                print("new room")
                sql = "INSERT INTO connection values(%d,'%s','%s','%s',1)" % (int(Room_No), Name, Password, date)
                print(sql)
                db_lock.acquire()
                cursor.execute(sql)
                db.commit()
                db_lock.release()
                print("insert done")
            else:
                print("room exists")
                sql = "UPDATE connection SET is_alive=1 WHERE room_no=%d and name='%s' and pwd='%s'and " \
                      "login_time between '%s' and '%s'" % (int(Room_No), Name, Password, start, end)
                print(sql)
                db_lock.acquire()
                cursor.execute(sql)
                db.commit()
                db_lock.release()
                print("update done")
            #return True

    def insertmes(self,name,pwd):
        sql = "insert into usr(name,pwd) value ('%s','%s')" %(name,pwd)

        # 互斥访问，预防并发访问时游标被占用，结果出错
        db_lock.acquire()
        cursor.execute(sql)
        db_lock.release()#释放锁
        db.commit()
        print("插入数据")
        return '登记成功'
