# -*- coding: utf-8 -*-
from client import c
class S_LoginController:
    def Login(self,id,pwd):
        #print('in contro')
        if len(id)==0:
            return False,'输入用户名不应为空'
        if len(pwd)==0:
            return False, '输入密码不应为空'
        res = True
        message = '登录成共'
        #调用communication的实例c  c.AC_Req(1,2)
        return res,message