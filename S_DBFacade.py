# -*- coding: utf-8 -*-
import re
import MySQLdb
import sys
import threading
'''
主动执行这个文件的话是用sqlToTxt把数据库里面的内容全部抽取到txt里面，
通过函数webToText则是一次把一条记录分别插入txt
'''
#多线程访问互斥锁
db_lock = threading.Lock()

# 打开数据库连接
db = MySQLdb.connect(host="localhost", port=3306, user="root", password="", db="software_serv", charset="utf8")
cursor = db.cursor()
print("连接数据库")


def db_close():
    #关闭数据库
    print ("关闭数据库")
    db.close()