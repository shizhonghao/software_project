# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from views.servent import S_login,S_Cost
from models.servent import HeartBeat,Sensor
from controller.servent.S_CostController import S_CostController
import untitled


class Ui_MainWindow(object):

    def __init__(self):
        #每个界面的初始定义，信号连接
        #由于centralwidget还没有定义，setupUi放到之后在做
        self.loginUI = S_login.Ui_Form()
        self.loginUI._haslogged.connect(self.logged)

        self.costUI = S_Cost.Ui_Form()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        #centralwidget, MainWindow自带的大作画区
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 120, 311, 131))
        self.label.setObjectName("label")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(80, 290, 241, 101))
        self.pushButton2.setObjectName("pushButton2")
        # 这个是槽函数，形式就是： 实体.信号函数名.connect(回调函数名)
        # 如果要使用额外的传参，回调函数写成lambda表达式就可以了
        self.pushButton2.clicked.connect(self.showLogin)
        self.pushButton2.setText("S_login")
        S_login.Ui_Form.setupUi(self.loginUI, self.centralwidget)
        self.loginUI.hide()
        self.costUI.setupUi(self.centralwidget)

        self.costUI.hide()

        self.widget=self.costUI

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(80, 190, 241, 101))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.clicked.connect(self.showCost)
        #这个是槽函数，形式就是： 实体.信号函数名.connect(回调函数名)
        #如果要使用额外的传参，回调函数写成lambda表达式就可以了


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "this is the MainWindow"))

    def showStatusDisplay(self):
        # 对接再说，展示界面
        self.pushButton3.setText('now is StatusDisplay')


    #登录成功后，创建心跳类，还有传感器！！（因为传感器的时间间隔是恒定的）
    #可能还要在这里创建从机类。。
    def logged(self):
        self.heart = HeartBeat.HeartBeat('pretend this is a servent')
        self.sensor = Sensor.Sensor('pretend this is a servent')
        self.showStatusDisplay()
        #self.cost_controller = S_CostController()
        #self.costUI

    def showLogin(self):
        self.widget.hide()
        self.widget = self.loginUI
        self.widget.show()

    def showCost(self):
        self.widget.hide()
        self.widget = self.costUI
        self.widget.show()

    #析构的时候中断通信
    def __del__(self):
        print("end the communication")
