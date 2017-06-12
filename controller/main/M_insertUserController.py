# -*- coding: utf-8 -*-

from models.main.UserRecord import UserRecord
import re
class InsertUserController:
    def insert(self,roomNo,name,pwd):
        roomNoMatch = re.match(r'^[0-9][0-9]*$', roomNo, re.S | re.I)
        nameMatch = re.match(r'.*[\'\"\\].*', name, re.S | re.I)
        pwdMatch = re.match(r'^[0-9][0-9]*$', pwd, re.S | re.I)
        if len(roomNo) == 0:
            return  '输入房间号不应为空'
        elif roomNoMatch == None:
            return '房间号格式错误，只能包含数字'

        if len(name) == 0:
            return '输入用户名不应为空'
        elif nameMatch != None:
            return '用户名格式错误，含有非法字符(\',\",\\)'

        if len(pwd) == 0:
            return '输入密码不应为空'
        elif pwdMatch == None:
            return '密码格式错误，只能包含数字'
        return UserRecord.insertmes(UserRecord,roomNo,name,pwd)