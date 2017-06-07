# -*- coding: utf-8 -*-

from client import c

class S_BoardController:
    def __init__(self,servent):
       self.servent = servent
       c.wind_change_ac.connect(self.Wind_Change_deal)
    #温度设置
    def T_raise(self,delta):
        #直接修改数据类
        print("T_raise into controller")
        self.servent.update_sys(delta,self.servent.targetW,self.sysModel)
        print("T_raise")
    #风速设置
    def Wind_Change(self,level):
        #调用通信类发信息
        self.servent.update_sys(self.servent.targetT, level, self.sysModel)
        c.AC_Req(level,self.servent.start_blowing)
        print("Wind_Change")

    def Wind_Change_deal(self,Level,Start_Blowing):
        self.servent.update_rw(Level,Start_Blowing)

    #状态查询
    def getCurrentState(self):
        self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing = self.servent.ret_current_state()
        self.check_rt()
        return self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing
    #温度检测
    def check_rt(self):
        if(-1< self.sysT - self.targetT and self.sysT - self.targetT < 1 ):
            if(self.start_blowing == 1):
                #调用通信类发信息
                c.AC_Req(self.sysW, 0)
                print("温度到达 待机ing")
        else:
            if(self.start_blowing == 0):
                #调用通信类发信息
                c.AC_Req(self.sysW, 1)
                print("重新开机")

