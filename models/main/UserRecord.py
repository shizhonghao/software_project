# -*- coding: utf-8 -*-

from M_database import cursor,db_lock,db
from PyQt5.QtCore import pyqtSignal,QObject
from datetime import datetime
import re

class UserRecord(QObject):
    __tablename__ = 'usr'
    log_sig = pyqtSignal(str, int, str, str)

    def Check(self, Room_No, Name, Password):
        print("check:", Room_No, Name, Password)

        #检查房间号/用户名/身份证是否含有非法字符
        numMatch = re.match(r'^[0-9][0-9]*$', Room_No, re.S | re.I)
        idMatch = re.match(r'.*[\'\"\\].*', Name, re.S | re.I)
        pwdMatch = re.match(r'.*[\'\"\\].*', Password, re.S | re.I)
        #含有非法字符则弹回去，防止崩溃
        if numMatch == None:
            self.log_sig.emit(Room_No, 0, Name, Password)
            return False
        if idMatch != None:
            self.log_sig.emit(Room_No, 0, Name, Password)
            return False
        elif pwdMatch != None:
            self.log_sig.emit(Room_No, 0, Name, Password)
            return False
        db_lock.acquire()
        sql = "SELECT * FROM " + self.__tablename__ + " WHERE roomNo=%d and name='%s' and pwd='%s'" % (int(Room_No),Name, Password)
        print(sql)
        cursor.execute(sql)
        row = cursor.fetchone()
        db_lock.release()
        print(row)
        if row == None:
            print("not connected")
            self.log_sig.emit(Room_No, 0, Name, Password)
            return False
            #return False
        else:
            print("connected")
            date = datetime.now()
            start = datetime(date.year, date.month, date.day, 0, 0, 0)
            end = datetime(date.year, date.month, date.day, 23, 59, 59)
            db_lock.acquire()
            sql = "SELECT is_alive FROM connection WHERE room_no=%d and login_time between '%s' and '%s'" % (int(Room_No), start, end)
            cursor.execute(sql)
            row = cursor.fetchone()
            db_lock.release()
            if row == None:
                self.log_sig.emit(Room_No, 1, Name, Password)
                print("new room")
                sql = "INSERT INTO connection values(%d,'%s','%s','%s',1)" % (int(Room_No), Name, Password, date)
                print(sql)
                db_lock.acquire()
                cursor.execute(sql)
                db.commit()
                db_lock.release()
                print("insert done")
                return True
            elif row[0]==0:
                self.log_sig.emit(Room_No, 1, Name, Password)
                print("room exists and not connect")
                sql = "UPDATE connection SET is_alive=1 WHERE room_no=%d and name='%s' and pwd='%s'and " \
                      "login_time between '%s' and '%s'" % (int(Room_No), Name, Password, start, end)
                print(sql)
                db_lock.acquire()
                cursor.execute(sql)
                db.commit()
                db_lock.release()
                print("update done")
                return True
            else: #(房间已经被登录)
                self.log_sig.emit(Room_No, 0, Name, Password)
                return False
            #return True

    def insertmes(self,roomNo,name,pwd):
        sql = "insert into usr(roomNo,name,pwd) value (%d,'%s','%s')" %(int(roomNo),name,pwd)
        print(sql)
        # 互斥访问，预防并发访问时游标被占用，结果出错
        db_lock.acquire()
        cursor.execute(sql)
        db_lock.release()#释放锁
        db.commit()
        print("插入数据")
        return '登记成功'
