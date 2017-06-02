# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

import untitled
from views.main import M_login
from models.main.SubMatch import queue


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        #centralwidget, MainWindow自带的大作画区
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 120, 311, 131))
        self.label.setObjectName("label")

        ##这是一个子界面类！不是一个实际的widget类！要自己重写hide,show方法
        self.widget = untitled.Ui_Form()
        #初始化这个创建的子界面类
        untitled.Ui_Form.setupUi(self.widget,self.centralwidget)
        self.widget.hide()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 390, 241, 101))
        self.pushButton.setObjectName("pushButton")
        #这个是槽函数，形式就是： 实体.信号函数名.connect(回调函数名)
        #如果要使用额外的传参，回调函数写成lambda表达式就可以了
        self.pushButton.clicked.connect(lambda:self.widget.show('change it'))

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(80, 290, 241, 101))
        self.pushButton2.setObjectName("pushButton2")
        # 这个是槽函数，形式就是： 实体.信号函数名.connect(回调函数名)
        # 如果要使用额外的传参，回调函数写成lambda表达式就可以了
        self.pushButton2.clicked.connect(self.showLogin)
        self.pushButton2.setText("M_login")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(80, 190, 241, 101))
        self.pushButton3.setObjectName("pushButton3")
        #这个是槽函数，形式就是： 实体.信号函数名.connect(回调函数名)
        #如果要使用额外的传参，回调函数写成lambda表达式就可以了
        self.pushButton3.clicked.connect(lambda:self.widget.show('change it'))

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
        self.pushButton.setText(_translate("MainWindow", "show dialog"))

    def showStatusDisplay(self):
        # 对接再说，展示界面
        self.pushButton3.setText('now is StatusDisplay')

    def showLogin(self):
        self.widget = M_login.Ui_Form()
        self.widget._haslogged.connect(self.showStatusDisplay)
        M_login.Ui_Form.setupUi(self.widget, self.centralwidget)
        self.widget.show()


