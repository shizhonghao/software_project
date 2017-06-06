# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outside.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from views.servent.infoshow import Ui_S_Board
from views.servent.S_Cost import Ui_S_Cost
from views.servent.S_login import Ui_S_Login
from models.servent import HeartBeat,Sensor
from models.servent.servent import S_servent,myroom

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ShutDown = QtWidgets.QPushButton(self.centralwidget)
        self.ShutDown.setGeometry(QtCore.QRect(720, 0, 75, 23))
        self.ShutDown.setObjectName("ShutDown")
        self.InfoShow = QtWidgets.QPushButton(self.centralwidget)
        self.InfoShow.setGeometry(QtCore.QRect(70, 0, 75, 23))
        self.InfoShow.setObjectName("InfoShow")
        self.CostShow = QtWidgets.QPushButton(self.centralwidget)
        self.CostShow.setGeometry(QtCore.QRect(140, 0, 75, 23))
        self.CostShow.setObjectName("CostShow")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(3, 0, 71, 21))
        self.label.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 新建信息显示界面
        self.boardwidget = Ui_S_Board()
        self.boardwidget.setupUi(self.centralwidget)
        self.boardwidget.hide()

        # 新建登录界面
        self.loginwidget = Ui_S_Login()
        self.loginwidget.setupUi(self.centralwidget)
        self.loginwidget.show()
        self.loginwidget._haslogged.connect(self.logged)

        # 新建账单显示界面
        self.costwidget = Ui_S_Cost()
        self.costwidget.setupUi(self.centralwidget)
        self.costwidget.hide()


        # 信号与槽
        self.InfoShow.clicked.connect(self.infoshow_clk)   #信息展示
        self.CostShow.clicked.connect(self.costshow_clk)   #账单展示
        self.ShutDown.clicked.connect(self.shutdown_request)   #关机请求
        #关机成功信号，关闭窗口or回到登录界面？

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ShutDown.setText(_translate("MainWindow", "关机"))
        self.InfoShow.setText(_translate("MainWindow", "信息展示"))
        self.CostShow.setText(_translate("MainWindow", "账单展示"))
        self.label.setText(_translate("MainWindow", "房间号"))

    #信息展示
    def infoshow_clk(self):
        self.costwidget.hide()
        self.boardwidget.show()

    #账单展示
    def costshow_clk(self):
        self.boardwidget.hide()
        self.costwidget.show()

    #关机请求
    def shutdown_request(self):
        print("shurdown_request")
        #与主机通信

    # 登录成功后，创建心跳类，还有传感器！！（因为传感器的时间间隔是恒定的）
    # 可能还要在这里创建从机类。。
    def logged(self,Name,Password,Mode):
        # 初始化一个servent,修改py文件中的单例指向这个实例
        myroom = S_servent(Name,Password,Mode)
        print(myroom.usr)
        self.heart = HeartBeat.HeartBeat('pretend this is a servent')
        self.sensor = Sensor.Sensor('pretend this is a servent')
        self.infoshow_clk()

    #关机处理
    #def shutdown_ok(self):
