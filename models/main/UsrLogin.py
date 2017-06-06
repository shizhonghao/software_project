# -*- coding: utf-8 -*-
from M_database import cursor,db_lock
from server import server

class UsrLogin:
    __tablename__ = 'usr'
    def Check(self,Room_No,Name,Password):
        db_lock.acquire()
        sql = "SELECT * FROM " + self.__tablename__ + " WHERE name='%s' and pwd='%s'" % (Name, Password)
        cursor.execute(sql)
        row = cursor.fetchone()
        db_lock.release()
        print(row)
        if row==None:
            server.Login_ACK(Room_No, 0, Name, Password, Mode)
        else:
            server.Login_ACK(Room_No, 1, Name, Password, Mode)
