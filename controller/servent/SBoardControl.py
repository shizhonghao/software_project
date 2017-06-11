# -*- coding: utf-8 -*-

from client import c
from PyQt5.QtCore import pyqtSignal,QObject

class S_BoardController(QObject):
    _modelchanged = pyqtSignal()
    sendcnt = 0

    def __init__(self,servent):
       super().__init__()
       self.servent = servent
       c.wind_change_ac.connect(self.Wind_Change_deal)
       c.fare_info_change.connect(self.Cost_Change_deal)
       c._model_change.connect(self.Model_Change_deal)

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
        c.AC_Req(self.servent.start_blowing,level)
        print("Wind_Change")

    def Wind_Change_deal(self,Level,Start_Blowing):
        print(Level,Start_Blowing)
        self.servent.update_rw(Level,Start_Blowing)

    def Cost_Change_deal(self,Fare,Energy):
        self.servent.update_cost(Fare,Energy)

    def Model_Change_deal(self,Heater):
        print("收到模式切换")
        if(self.servent.sysModel != Heater): #仅当当前从机记录的工作模式与广播不符合的时候才变化
            # 根据系统工作模式调整从机目标温度
            if self.Heater == 1 and self.targetT<25:  # 冬季，制热
                self.targetT = 28.0
                self.targetW = 0
                self._modelchanged.emit()
            elif self.Heater == 0 and self.targetT>25:
                self.targetT = 22.0
                self.targetW = 0
                self._modelchanged.emit()
            
            self.servent.update_sys(self.targetT,self.targetW,self.sysModel)

    #状态查询
    def getCurrentState(self):
        self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing = self.servent.ret_current_state()
        self.check_rt()
        return self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing
    #温度检测
    def check_rt(self):
        self.sendcnt +=1
        self.sendcnt %=3
        #if self.sendcnt != 0:
        #    return
        if(self.servent.sysModel == 1):#制热时，室温大等于目标温度则待机，小于1度且停风时请求
            if (self.sysT - self.targetT >= 0):
                if (self.start_blowing == 1):
                    # 调用通信类发信息
                    c.AC_Req(0, self.targetW)
                    print("温度到达 待机ing")
            elif(self.sysT - self.targetT < -1):
                if (self.start_blowing == 0):
                    # 调用通信类发信息
                    c.AC_Req(1, self.targetW)
                    print("重新开机")

        if(self.servent.sysModel == 0):#制冷时，室温小等于目标温度则待机，大于1度且停风时请求
            if (self.sysT - self.targetT <= 0):
                if (self.start_blowing == 1):
                    # 调用通信类发信息
                    c.AC_Req(0, self.targetW)
                    print("温度到达 待机ing")
            elif(self.sysT - self.targetT > 1):
                if (self.start_blowing == 0):
                    # 调用通信类发信息
                    c.AC_Req(1, self.targetW)
                    print("重新开机")

