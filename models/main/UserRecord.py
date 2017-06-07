# -*- coding: utf-8 -*-

from M_database import cursor,db_lock,db
class UserRecord:
    def insertmes(self,name,pwd):
        sql = "insert into usr(name,pwd) value ('%s','%s')" %(name,pwd)

        # 互斥访问，预防并发访问时游标被占用，结果出错
        db_lock.acquire()
        cursor.execute(sql)
        db_lock.release()#释放锁
        db.commit()
        print("插入数据")
        return '登记成功'
