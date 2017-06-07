# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_submonitor.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from controller.main import M_SubStatusController
import time  ##测试用


class Ui_SubMonitor(object):
    def __init__(self):
        self.messagelist = []
        self.sub = M_SubStatusController.SubStatuController()

    def setupUi(self, MainWindow):
        self.SubMonitor = QWidget(MainWindow)
        self.SubMonitor.setObjectName("SubMonitor")
        self.SubMonitor.resize(990, 500)
        self.SubMonitor.setGeometry(QtCore.QRect(30, 30, 990, 500))

        self.stack = QtWidgets.QStackedWidget(self.SubMonitor)
        self.stack.setGeometry(QtCore.QRect(30, 30, 800, 400))

        # self.showWidget=QWidget(self.SubMonitor)
        # self.showWidget.setObjectName("showWidget")
        # self.showWidget.resize(800,400)
        # self.showWidget.setGeometry(QtCore.QRect(30,30,800,400))


        # self.monitorWidget = QtWidgets.QWidget(self.centralwidget)
        # self.monitorWidget.setGeometry(QtCore.QRect(30, 30, 991, 501))
        # self.monitorWidget.setObjectName("monitorWidget")


        self.labeltest = QtWidgets.QLabel(self.SubMonitor)
        self.labeltest.setGeometry(QtCore.QRect(20, 30, 81, 18))
        self.labeltest.setObjectName("labeltest")

        self.updateData()

        ''''
        self.listlayout1 = QtWidgets.QVBoxLayout(self.showWidget)  ##垂直排列
        ###加for循环，room数####
        x=0
        self.messagelist=self.sub.showSub()
        print(self.messagelist)
        while x<len(self.messagelist):
        ###while x <3:
            print("a")
            self.roomnoLabel = QtWidgets.QLabel()
            self.idLabel=QtWidgets.QLabel()
            self.statuLabel = QtWidgets.QLabel()
            self.tempLabel = QtWidgets.QLabel()
            self.veloLabel = QtWidgets.QLabel()

            ###test过后删除###
            self.roomnoLabel.setText("No.1")
            self.idLabel.setText("xx")
            self.statuLabel.setText("工作中")
            self.tempLabel.setText("33℃")
            self.veloLabel.setText("中速")


            self.roomnoLabel.setNum(self.messagelist[x][0])
            self.idLabel.setText(self.messagelist[x][1])
            self.statuLabel.setNum(self.messagelist[x][2])
            self.tempLabel.setNum(self.messagelist[x][3])
            self.veloLabel.setNum(self.messagelist[x][4])



            self.rowlayout = QtWidgets.QHBoxLayout()
            self.rowlayout.addWidget(self.roomnoLabel)
            self.rowlayout.addWidget(self.idLabel)
            self.rowlayout.addWidget(self.statuLabel)
            self.rowlayout.addWidget(self.tempLabel)
            self.rowlayout.addWidget(self.veloLabel)

            self.listlayout1.addLayout(self.rowlayout)
            x+=1

        self.showWidget.setLayout(self.listlayout1)
        '''

        self.retranslateUi(self.SubMonitor)
        QtCore.QMetaObject.connectSlotsByName(self.SubMonitor)

    def retranslateUi(self, SubMonitor):
        _translate = QtCore.QCoreApplication.translate
        SubMonitor.setWindowTitle(_translate("SubMonitor", "Form"))
        self.labeltest.setText(_translate("SubMonitor", "监视界面"))
   ########刷新数据#########
    def updateData(self):
        x = self.stack.count()
        print("xxxxxxx", x)
        if (x != 0):
            i = 0
            while i < x:
                test = self.stack.widget(i)
                self.stack.removeWidget(test)
                test.destroy()
                print("enenene")
                i += 1
                x = self.stack.count()
                print("xxxxxxx", x)
        x = self.stack.count()
        print("xxxxxxx", x)
        showWidget = QWidget(self.SubMonitor)
        showWidget.resize(800, 400)
        print("##############33333")
        self.messagelist = self.sub.showSub()
        str = time.asctime()
        list = [1, str, 3, 4, 5]
        self.messagelist.append(list)
        print("hhhhhh")
        print(self.messagelist)

        listlayout1 = QtWidgets.QVBoxLayout(showWidget)  ##垂直排列
        ###加for循环，room数####
        x = 0
        # self.messagelist = self.sub.showSub()
        # print(self.messagelist)
        while x < len(self.messagelist):
            ###while x <3:
            print("a")
            roomnoLabel = QtWidgets.QLabel()
            idLabel = QtWidgets.QLabel()
            statuLabel = QtWidgets.QLabel()
            tempLabel = QtWidgets.QLabel()
            veloLabel = QtWidgets.QLabel()

            ###test过后删除###
            '''
            self.roomnoLabel.setText("No.1")
            self.idLabel.setText("xx")
            self.statuLabel.setText("工作中")
            self.tempLabel.setText("33℃")
            self.veloLabel.setText("中速")
            '''

            roomnoLabel.setNum(self.messagelist[x][0])
            idLabel.setText(self.messagelist[x][1])
            statuLabel.setNum(self.messagelist[x][2])
            tempLabel.setNum(self.messagelist[x][3])
            veloLabel.setNum(self.messagelist[x][4])

            rowlayout = QtWidgets.QHBoxLayout()
            rowlayout.addWidget(roomnoLabel)
            rowlayout.addWidget(idLabel)
            rowlayout.addWidget(statuLabel)
            rowlayout.addWidget(tempLabel)
            rowlayout.addWidget(veloLabel)

            listlayout1.addLayout(rowlayout)
            x += 1

        showWidget.setLayout(listlayout1)
        self.stack.addWidget(showWidget)
        # self.stack.setCurrentWidget(showWidget)
        x = self.stack.count()
        print("xxxxxxx", x)






