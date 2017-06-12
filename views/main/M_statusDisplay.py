# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_statusdisplay.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from controller.main import M_StatusController
from PyQt5.QtCore import pyqtSignal,QTimer

class Ui_StatusDisplay(QWidget):

    _changedFreq = pyqtSignal(int)

    mtemp=0.00
    mvelocity=0
    controller=M_StatusController.StatusController()
    mfreq=0
    mstrat=0
    mconnec=[]
    mstatus=""

    def setupUi(self, MainWindow):
        self.reflashTimer = QTimer()
        self.reflashTimer.setInterval(2000)
        self.reflashTimer.timeout.connect(self.showCurrentRoom)
        self.reflashTimer.start()

        self.StatusDisplay=QWidget(MainWindow)
        self.StatusDisplay.setObjectName("StatusDisplay")
        self.StatusDisplay.resize(990, 500)
        self.StatusDisplay.setGeometry(QtCore.QRect(30,30,990,500))
        '''
        self.defaultWidget = QtWidgets.QWidget(self.StatusDisplay)
        self.defaultWidget.setGeometry(QtCore.QRect(30, 30, 991, 501))
        self.defaultWidget.setObjectName("defaultWidget")
       '''
        self.statusWidget = QtWidgets.QWidget(self.StatusDisplay)
        self.statusWidget.setGeometry(QtCore.QRect(50, 40, 391, 421))
        self.statusWidget.setObjectName("statusWidget")

        self.label = QtWidgets.QLabel(self.statusWidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 18))
        self.label.setObjectName("label")
        self.tempLabel=QtWidgets.QLabel(self.statusWidget)
        self.tempLabel.setGeometry(QtCore.QRect(130, 30, 81, 18))
        self.tempLabel.setObjectName("tempLabel")

        self.label_2 = QtWidgets.QLabel(self.statusWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 81, 18))
        self.label_2.setObjectName("label_2")
        self.veloLabel=QtWidgets.QLabel(self.statusWidget)
        self.veloLabel.setGeometry(QtCore.QRect(130, 120, 81, 18))
        self.veloLabel.setObjectName("veloLabel")

        self.label_3 = QtWidgets.QLabel(self.statusWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 81, 18))
        self.label_3.setObjectName("label_3")
        self.statuslabel = QtWidgets.QLabel(self.statusWidget)
        self.statuslabel.setGeometry(QtCore.QRect(100, 250, 81, 18))
        self.statuslabel.setObjectName("statuslabel")
        self.modelRadioButton = QtWidgets.QRadioButton(self.statusWidget)
        self.modelRadioButton.setGeometry(QtCore.QRect(20, 360, 132, 22))
        self.modelRadioButton.setObjectName("radioButton")
        self.modelRadioButton.setText("制冷")

        self.modelRadioButton_2 = QtWidgets.QRadioButton(self.statusWidget)
        self.modelRadioButton_2.setGeometry(QtCore.QRect(150, 360, 132, 22))
        self.modelRadioButton_2.setObjectName("radioButton_2")
        self.modelRadioButton_2.setText("制热")

        self.ModelStraconfButton = QtWidgets.QPushButton(self.statusWidget)
        self.ModelStraconfButton.setGeometry(QtCore.QRect(270, 360, 112, 34))
        self.ModelStraconfButton.setObjectName("straconfButton")
        self.ModelStraconfButton.setText("模式修改")
        self.ModelStraconfButton.clicked.connect(self.on_ModelButton_clicked)

        self.roomWidget = QtWidgets.QWidget(self.StatusDisplay)
        self.roomWidget.setGeometry(QtCore.QRect(540, 40, 391, 200))
        self.roomWidget.setObjectName("roomWidget")

        self.label_4 = QtWidgets.QLabel(self.roomWidget)
        self.label_4.setGeometry(QtCore.QRect(0, 30, 141, 21))
        self.label_4.setObjectName("label_4")
        self.roomLabel=QtWidgets.QLabel(self.roomWidget)
        self.roomLabel.setGeometry(QtCore.QRect(0, 80, 100, 200))
        self.roomLabel.setObjectName("roomLabel")

        ##############获取频率——spinbox############
        self.freqSpinbox = QtWidgets.QSpinBox(self.StatusDisplay)
        self.freqSpinbox.setGeometry(QtCore.QRect(550, 400, 80, 40))
        self.freqSpinbox.setObjectName("freqSpinbox")
        self.freqSpinbox.setRange(1, 20)

        self.freqButton = QtWidgets.QPushButton(self.StatusDisplay)
        self.freqButton.setGeometry(QtCore.QRect(800, 400, 112, 34))
        self.freqButton.setObjectName("freqButton")

       # self.freqButton.clicked.connect(self.freqChanged)
        ##############获取策略——RadioButton#################
        self.statuWidget = QtWidgets.QWidget(self.StatusDisplay)
        self.statuWidget.setGeometry(QtCore.QRect(540, 180, 391, 200))
        self.statuWidget.setObjectName("statuWidget")

        self.label_5 = QtWidgets.QLabel(self.statuWidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 51, 18))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("当前策略：")
        self.stratlabel = QtWidgets.QLabel(self.statuWidget)
        self.stratlabel.setGeometry(QtCore.QRect(130, 0, 151, 18))
        self.stratlabel.setObjectName("stratlabel")

        self.radioButton = QtWidgets.QRadioButton(self.statuWidget)
        self.radioButton.setGeometry(QtCore.QRect(0, 100, 132, 22))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.statuWidget)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 100, 132, 22))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.statuWidget)
        self.radioButton_3.setGeometry(QtCore.QRect(260, 100, 132, 22))
        self.radioButton_3.setObjectName("radioButton_3")

        self.straconfButton = QtWidgets.QPushButton(self.statuWidget)
        self.straconfButton.setGeometry(QtCore.QRect(140, 150, 112, 34))
        self.straconfButton.setObjectName("straconfButton")

        self.showMes()

        self.straconfButton.clicked.connect(self.on_tellmeButton_clicked)

        # ################频率微调和滑块信号槽#############
        # self.freqSlider.valueChanged.connect(self.freqSpinbox.setValue)
        self.freqButton.clicked.connect(self.freqChanged)

        self.retranslateUi(self.StatusDisplay)
        QtCore.QMetaObject.connectSlotsByName(self.StatusDisplay)

    def on_tellmeButton_clicked(self):
        #print("radio changed")
        if (self.radioButton.isChecked()):
            self.controller.strat=1
        if (self.radioButton_2.isChecked()):
            self.controller.strat=2
        if (self.radioButton_3.isChecked()):
            self.controller.strat=3
        self.controller.changeStrat()
        self.showMes()

    def on_ModelButton_clicked(self):
        if (self.modelRadioButton.isChecked()):
            self.controller.changeStatus(0)
        if (self.modelRadioButton_2.isChecked()):
            self.controller.changeStatus(1)
        self.showMes()

    def freqChanged(self):
        self.controller.freq=int(self.freqSpinbox.value())
        print("to change freq as %d" % (self.controller.freq))
        self._changedFreq.emit(self.controller.freq)
        self.controller.changeFreq()


    def retranslateUi(self, StatusDisplay):
        _translate = QtCore.QCoreApplication.translate
        StatusDisplay.setWindowTitle(_translate("StatusDisplay", "Form"))
        self.straconfButton.setText(_translate("StatusDisplay", "确认"))
        self.freqButton.setText(_translate("StatusDisplay", "确认"))
        self.label.setText(_translate("StatusDisplay", "温度："))
        self.label_2.setText(_translate("StatusDisplay", "风速："))
        self.label_3.setText(_translate("StatusDisplay", "工作模式："))
        self.radioButton.setText(_translate("StatusDisplay", "时间片轮询"))
        self.radioButton_2.setText(_translate("StatusDisplay", "高速风优先"))
        self.radioButton_3.setText(_translate("StatusDisplay", "先来先服务"))
        self.label_4.setText(_translate("StatusDisplay", "当前连接房间："))

    def showMes(self):
        del self.mconnec[:]
        self.controller.getFreq()
        self.controller.getStrat()
        print("status is ",self.controller.getStatu())
        if(self.controller.getStatu()==0):
            self.mtemp=22.0
            self.modelRadioButton.setChecked(True)
            self.modelRadioButton_2.setChecked(False)
            self.statuslabel.setText("制冷")
        else:
            self.mtemp=28.0
            self.modelRadioButton.setChecked(False)
            self.modelRadioButton_2.setChecked(True)
            self.statuslabel.setText("制热")

        self.tempLabel.setText(str(self.mtemp)+'℃')
        if self.mvelocity==0:
            self.veloLabel.setText("低速")
        elif self.mvelocity==1:
            self.veloLabel.setText("中速")
        elif self.mvelocity==2:
            self.veloLabel.setText("高速")

        self.showCurrentRoom()
        #####刷新测试
        #self.roomLabel.setNum(time.clock())

        if self.controller.strat==1:
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(False)
            self.stratlabel.setText("时间片轮询")
        elif self.controller.strat==2:
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.radioButton_3.setChecked(False)
            self.stratlabel.setText("高速风优先抢占")
        elif self.controller.strat==3:
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.radioButton_3.setChecked(False)
            self.stratlabel.setText("先来先服务")

        self.freqSpinbox.setValue(self.controller.freq)

    def showCurrentRoom(self):
        list = self.controller.getConnec()
        x = 0
        connecstr = ""
        while x < len(list):
            connecstr += str(list[x])
            connecstr += "\n"
            x += 1
        self.roomLabel.setText(connecstr)
