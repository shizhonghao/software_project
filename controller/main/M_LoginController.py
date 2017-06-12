# -*- coding: utf-8 -*-
from models.main.Administrator import Administrator
import re
class M_LoginController:
    def Login(self,id,pwd):
        idMatch = re.match(r'.*[\'\"\\].*', id, re.S | re.I)
        pwdMatch = re.match(r'.*[\'\"\\].*', pwd, re.S | re.I)

        if len(id)==0:
            return False,'输入用户名不应为空'
        elif idMatch != None:
            return False, '用户名格式错误，含有非法字符(\',\",\\)'
        if len(pwd)==0:
            return False, '输入密码不应为空'
        elif pwdMatch != None:
            return False, '密码格式错误，含有非法字符(\',\",\\)'

        res,message = Administrator.select(Administrator(),id,pwd)
        return res,message