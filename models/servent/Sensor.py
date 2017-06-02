# -*- coding: utf-8 -*-
from PyQt5.QtCore import *


class Sensor:
    init_interval = 60000#一分钟更新一次还是怎样。。。

    def __init__(self, servent):
        # 定时器
        self.timer = QTimer()
        self.timer.setInterval(self.init_interval)
        self.timer.start()

        # 记下作为操作目标的从机状态类
        self.target = servent
        print('sensor set')
        self.timer.timeout.connect(self.state_update)

    def state_update(self):
        # 做状态更新
        '''
        应该是先调用下计算函数算下现在的温度
        然后通过self.target的set_temp之类的方法（接口去问）来更新它
        不用操作数据库！
        '''
        i = 2