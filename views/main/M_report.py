# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_report.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from datetime import datetime
from models.main.Request import Request

class Ui_Report(object):
    room = [int for i in range(0, 10)]
    type = 0
    currentRoom = 0
    currentDate = list([int for i in range(0, 3)])
    s_year = 0
    s_month = 0
    s_day = 0
    def setupUi(self, MainWidow):
        self.Report=QWidget(MainWidow)
        self.Report.setObjectName("Report")
        self.Report.resize(990, 500)
        self.Report.setGeometry(QtCore.QRect(30, 30, 990, 500))

        '''
        self.reportWidget = QtWidgets.QWidget(self.centralwidget)
        self.reportWidget.setGeometry(QtCore.QRect(30, 30, 991, 501))
        self.reportWidget.setObjectName("reportWidget")
        '''

        self.labeltest2 = QtWidgets.QLabel(self.Report)
        self.labeltest2.setGeometry(QtCore.QRect(20, 30, 81, 18))
        self.labeltest2.setObjectName("labeltest2")

        self.retranslateUi(self.Report)
        QtCore.QMetaObject.connectSlotsByName(self.Report)

        # 时间控件的初始化
        self.dateEdit = QtWidgets.QDateEdit(self.Report)
        self.dateEdit.setGeometry(QtCore.QRect(20, 20, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # 关于房号下拉菜单的初始化
        self.comboBox = QtWidgets.QComboBox(self.Report)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 87, 22))
        self.comboBox.setObjectName("comboBox")

        # 写开机次数的标签
        self.label = QtWidgets.QLabel(self.Report)
        self.label.setGeometry(QtCore.QRect(130, 60, 81, 21))
        self.label.setText("开机次数")
        # 显示开关机次数的格子
        self.lineEdit = QtWidgets.QLineEdit(self.Report)
        self.lineEdit.setGeometry(QtCore.QRect(220, 60, 51, 21))
        self.lineEdit.setObjectName("lineEdit")

        # 写着总费用的标签
        self.label_2 = QtWidgets.QLabel(self.Report)
        self.label_2.setGeometry(QtCore.QRect(310, 60, 72, 21))
        self.label_2.setText("总费用")
        # 显示总费用的格子
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Report)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 60, 61, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        # 用来放所有的记录的表格
        self.tableWidget = QtWidgets.QTableWidget(self.Report)
        self.tableWidget.setGeometry(QtCore.QRect(130, 120, 700, 200))
        self.tableWidget.setObjectName("tableWidget")
        # 设置对用户只读
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 表格列数设置
        self.tableWidget.setColumnCount(8)
        # 表格列宽设置
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 表格列名设置
        self.tableWidget.setHorizontalHeaderLabels(['房间号', '开始时间', '停止时间', '起始温度', '停止温度', '起始风速', '停止风速', '费用'])

        # 写着请求记录的标签
        self.label_3 = QtWidgets.QLabel(self.Report)
        self.label_3.setGeometry(QtCore.QRect(130, 90, 72, 21))
        self.label_3.setObjectName("label_3")

        # 选择报表类型的按钮
        self.pushButton = QtWidgets.QPushButton(self.Report)
        self.pushButton.setGeometry(150, 10, 93, 28)
        self.pushButton.setText("日报表")
        self.pushButton_1 = QtWidgets.QPushButton(self.Report)
        self.pushButton_1.setGeometry(280, 10, 93, 28)
        self.pushButton_1.setText("周报表")
        self.pushButton_2 = QtWidgets.QPushButton(self.Report)
        self.pushButton_2.setGeometry(410, 10, 93, 28)
        self.pushButton_2.setText("月报表")

        '''
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        '''
        # 将各事件与触发的槽函数相关联
        self.comboBox.activated.connect(self.comboboxSlot)
        self.dateEdit.dateChanged.connect(self.dateEditSlot)
        self.pushButton.clicked.connect(self.pushSlot)
        self.pushButton_1.clicked.connect(self.push1Slot)
        self.pushButton_2.clicked.connect(self.push2Slot)

    def retranslateUi(self, Report):
        _translate = QtCore.QCoreApplication.translate
        Report.setWindowTitle(_translate("Report", "Form"))
        self.labeltest2.setText(_translate("Report", "报表界面"))
        #self.label.setText(_translate("Report", "开关机次数"))
        #self.label_2.setText(_translate("Report", "总费用"))
        #self.label_3.setText(_translate("Report", "请求记录"))

    #初始化界面数据
    def iniUiReport(self):
        # 设置当前时间
        now = datetime.now()
        self.currentDate[0] = now.year
        self.currentDate[1] = now.month
        self.currentDate[2] = now.day + 1
        self.s_year = now.year
        self.s_month = now.month
        self.s_day = now.day
        if (self.currentDate[1] == 12 and self.currentDate[2] == 32):
            self.currentDate[0] = now.year + 1
            self.currentDate[1] = 1
            self.currentDate[2] = 1
        elif (self.currentDate[1] == 2):
            if (now.year % 4 == 0 and self.currentDate[2] == 30):
                self.currentDate[1] = 3
                self.currentDate[2] = 1
            elif (self.currentDate[2] == 29):
                self.currentDate[1] = 3
                self.currentDate[2] = 1
        elif ((self.currentDate[1] == 4 or self.currentDate[1] == 6 or self.currentDate[1] == 9 or self.currentDate[
            1] == 11) and self.currentDate[2] == 31):
            self.currentDate[1] = now.month + 1
            self.currentDate[2] = 1
        elif (self.currentDate[2] == 32):
            self.currentDate[2] = 1
            self.currentDate[1] = now.month + 1

        #默认房间设置
        self.comboBox.clear()
        room = Request.getRoomNo(Request())
        roomLen = len(room)
        i = 0
        if (roomLen != 0):
            self.currentRoom = room[0]
        while (i < roomLen):
            self.comboBox.addItem(str(room[i]))
            self.room[i] = room[i]
            i = i + 1

        # 设置默认显示时的房间的开机次数
        if (self.currentRoom != 0):
            switch_cnt = Request.getSwitchCnt(Request(), self.currentRoom,"%s-%s-%s" % (str(self.s_year), str(self.s_month), str(self.s_day)),"%s-%s-%s" % (str(self.currentDate[0]), str(self.currentDate[1]),str(self.currentDate[2])))
            self.lineEdit.setText(str(switch_cnt))

        # 设置默认显示时的房间总费用
        if (self.currentRoom != 0):
            cost = Request.getCost(Request(), self.currentRoom,"%s-%s-%s" % (str(self.s_year), str(self.s_month), str(self.s_day)), "%s-%s-%s" % (str(self.currentDate[0]), str(self.currentDate[1]), str(self.currentDate[2])))
            self.lineEdit_2.setText(str(cost))

        # 查询默认显示的房间的所有请求
        if (self.currentRoom != 0):
            request = Request.getRequest(Request(), self.currentRoom,
                                         "%s-%s-%s" % (str(self.s_year), str(self.s_month), str(self.s_day)),
                                         "%s-%s-%s" % (str(self.currentDate[0]), str(self.currentDate[1]),
                                                       str(self.currentDate[2])))
            self.tableWidget.setRowCount(len(request))
            for i in range(0, len(request)):
                for j in range(0, 8):
                    if (request[i][j] != None):
                        newItem = QtWidgets.QTableWidgetItem(str(request[i][j]))
                        # 设置居中
                        newItem.setTextAlignment(4 | 8 * 16)
                        self.tableWidget.setItem(i, j, newItem)
        # 隐藏每行的表头
        self.tableWidget.verticalHeader().setVisible(False)

    #更新各项显示
    def updateView(self):
        # 更新开关机次数
        switch_cnt = Request.getSwitchCnt(Request(), self.currentRoom,"%s-%s-%s" % (str(self.s_year), str(self.s_month), str(self.s_day)),"%s-%s-%s" % (str(self.currentDate[0]), str(self.currentDate[1]), str(self.currentDate[2])))
        self.lineEdit.setText(str(switch_cnt))
        #else:
        #    self.lineEdit.setText("0")

        # 更新开销
        cost = Request.getCost(Request(), self.currentRoom,"%s-%s-%s" % (str(self.s_year), str(self.s_month), str(self.s_day)), "%s-%s-%s" % (str(self.currentDate[0]), str(self.currentDate[1]), str(self.currentDate[2])))
        self.lineEdit_2.setText(str(cost))

        # 更新请求
        request = Request.getRequest(Request(), self.currentRoom,"%s-%s-%s" % (str(self.s_year), str(self.s_month), str(self.s_day)), "%s-%s-%s" % (str(self.currentDate[0]), str(self.currentDate[1]), str(self.currentDate[2])))
        self.tableWidget.setRowCount(len(request))
        print(request)
        for i in range(0,len(request)):
            for j in range(0, 8):
                if (request[i][j] != None):
                    newItem = QtWidgets.QTableWidgetItem(str(request[i][j]))
                    # 设置居中
                    newItem.setTextAlignment(4 | 8 * 16)
                    self.tableWidget.setItem(i, j, newItem)

    #因combobox中的变化而触发的函数
    def comboboxSlot(self):
        self.currentRoom = self.room[self.comboBox.currentIndex()]
        print("%s chosen"%(str(self.currentRoom)))
        self.updateView()

    #修改时间后的更新函数
    def dateEditSlot(self):
        #更新时间
        time = ""
        i = 0
        j = 0
        flag = 0
        while(i < len(self.dateEdit.text())):
            while(self.dateEdit.text()[i] != '/' and flag == 0):
                time = time + self.dateEdit.text()[i]
                if(i + 1 == len(self.dateEdit.text())):
                    flag = 1
                else:
                    i = i + 1
            self.currentDate[j] = int(time)
            j = j + 1
            time = ""
            i = i + 1
        #更新页面时间
        if(self.type == 0):
            self.s_year = self.currentDate[0]
            self.s_month = self.currentDate[1]
            self.s_day = self.currentDate[2]
            self.currentDate[2] = self.currentDate[2] + 1
            if (self.currentDate[1] == 12 and self.currentDate[2] == 32):
                self.currentDate[0] = self.s_year + 1
                self.currentDate[1] = 1
                self.currentDate[2] = 1
            elif (self.currentDate[1] == 2):
                if (self.s_year % 4 == 0 and self.currentDate[2] == 30):
                    self.currentDate[1] = 3
                    self.currentDate[2] = 1
                elif (self.currentDate[2] == 29):
                    self.currentDate[1] = 3
                    self.currentDate[2] = 1
            elif ((self.currentDate[1] == 4 or self.currentDate[1] == 6 or self.currentDate[1] == 9 or self.currentDate[1] == 11) and self.currentDate[2] == 31):
                self.currentDate[1] = self.s_month + 1
                self.currentDate[2] = 1
            elif (self.currentDate[2] == 32):
                self.currentDate[2] = 1
                self.currentDate[1] = self.s_month + 1
        elif(self.type == 1):#周报表
            self.s_year = self.currentDate[0]
            self.s_month = self.currentDate[1]
            self.s_day = self.currentDate[2] - 7
            if(self.s_day <= 0):
                if(self.s_month == 1):
                    self.s_year = self.s_year - 1
                    self.s_month = 12
                    self.s_day = self.s_day + 31
                elif(self.s_month == 3):
                    self.s_month = 2
                    if(self.s_year % 4 == 0):
                        self.s_day = self.s_day + 29
                    else:
                        self.s_day = self.s_day + 28
                elif(self.s_month == 5 or self.s_month == 7 or self.s_month == 10 or self.s_month == 12):
                    self.s_month = self.s_month - 1
                    self.s_day = self.s_day + 30
                else:
                    self.s_month = self.s_month - 1
                    self.s_day = self.s_day + 31
        elif(self.type == 2):
            self.s_year = self.currentDate[0]
            self.s_month = self.currentDate[1] -1
            self.s_day = self.currentDate[2]
            if(self.s_month == 0):
                self.s_year = self.s_year - 1
                self.s_month = 12
            elif(self.s_month == 2 and self.s_day > 28):
                if(self.s_year % 4 == 0):
                    self.s_day = 29
                else:
                    self.s_day = 28
            elif(self.s_day == 31):
                if(self.s_month == 4 or self.s_month == 6 or self.s_month == 9 or self.s_month == 11):
                    self.s_day = 30
        print("Time changed to %s-%s-%s" % (str(self.s_year),str(self.s_month),str(self.s_day)))
        #更新各部分显示
        self.updateView()

    #选择了日报表
    def pushSlot(self):
        print("啊，日报表")
        #更新报表类型
        self.type = 0
        #更新时间和各部分显示
        self.dateEditSlot()

    def push1Slot(self):
        print("啊，周报表")
        #修改报表类型
        self.type = 1
        #更新时间和各部分显示
        self.dateEditSlot()

    def push2Slot(self):
        print("啊，月报表")
        #修改报表类型
        self.type = 2
        #更新时间和各部分显示
        self.dateEditSlot()