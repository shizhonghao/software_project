# -*- coding: utf-8 -*-
from client import c
class S_LoginController:
    def Login(self,username,card_id):
        #print('in contro')
        if len(username)==0:
            return False,'输入用户名不应为空'
        if len(card_id)==0:
            return False, '输入身份证号不应为空'
        res = True
        message = '登录成功'
        #调用communication的实例c  c.AC_Req(1,2)
        return res,message