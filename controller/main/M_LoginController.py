# -*- coding: utf-8 -*-
from models.main.Administrator import Administrator
class M_LoginController:
    def Login(self,id,pwd):
        if len(id)==0:
            return False,'输入用户名不应为空'
        if len(pwd)==0:
            return False, '输入密码不应为空'
        res,message = Administrator.select(Administrator(),id,pwd)
        return res,message