# -*- coding: utf-8 -*-

from models.main.UserRecord import UserRecord
class InsertUserController:
    def insert(self,name,pwd):
        if len(name)==0:
            return '输入用户名不应为空'
        if len(pwd)==0:
            return '输入密码不应为空'
        return UserRecord.insertmes(UserRecord,name,pwd)