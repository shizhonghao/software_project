# -*- coding: utf-8 -*-

#from servent import S_servent

class S_BoardController:
    #def __init__(self):
    #   self.servent = S_servent()
    #温度设置
    def T_raise(self,delta):
        #调用通信类发信息
        print("T_raise")
    #风速设置
    def Wind_Change(self,level):
        #调用通信类发信息
        print("Wind_Change")
    #状态查询
    def getCurrentState(self):
        self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing = self.servent.ret_current_state()
        return self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing
    #温度检测
    def check_rt(self):
        if(-1< self.sysT - self.targetT and self.sysT - self.targetT < 1 ):
            if(self.start_blowing == 1):
                #调用通信类发信息
                print("温度到达 待机ing")
        else:
            if(self.start_blowing == 0):
                #调用通信类发信息
                print("重新开机")

