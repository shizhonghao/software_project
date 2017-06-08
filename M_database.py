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
db = MySQLdb.connect(host="localhost", port=3306, user="root", password="", db="software_proj", charset="utf8")
cursor = db.cursor()
print("连接数据库")

'''
            #取出这个商品的对应元组（由于json的限制最多只有5000条所以不会太占内存）
            cursor.execute(auctionSelect+result[0])
            row = cursor.fetchone()
            while row!=None:
                #逐行取出写txt文件
                #商品的评论
                fw_comment.write(row[0]+'\n')
                #商品的好 中 差评分级（ 1 0 -1）
                fw_level.write(str(row[1])+'\n')
                row = cursor.fetchone() #下一条
'''


def db_close():
    #关闭数据库
    print ("关闭数据库")
    db.close()

