# -*- coding: utf-8 -*-
from M_database import cursor
class Administrator:
    __tablename__ = 'administrators'

    def select(self,id,pwd):
        sql = "SELECT * FROM " +self.__tablename__+" WHERE id='%s' and pwd='%s'" %(id,pwd)
        cursor.execute(sql)
        row = cursor.fetchone()
        print(row)
        res = True
        message = '登录成功'
        if row==None: #没查到了管理员号
            res = False
            message ='账号或密码错误，请检查后重新登录'

        return res,message