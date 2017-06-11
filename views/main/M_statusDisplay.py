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
        self.reflashTimer.timeout.connect(self.showMes)
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
        self.label_2.setGeometry(QtCore.QRect(20, 220, 81, 18))
        self.label_2.setObjectName("label_2")
        self.veloLabel=QtWidgets.QLabel(self.statusWidget)
        self.veloLabel.setGeometry(QtCore.QRect(130, 220, 81, 18))
        self.veloLabel.setObjectName("veloLabel")

        self.label_3 = QtWidgets.QLabel(self.statusWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 360, 81, 18))
        self.label_3.setObjectName("label_3")
        self.statuLabel = QtWidgets.QLabel(self.statusWidget)
        self.statuLabel.setGeometry(QtCore.QRect(130, 360, 81, 18))
        self.statuLabel.setObjectName("statuLabel")

        self.roomWidget = QtWidgets.QWidget(self.StatusDisplay)
        self.roomWidget.setGeometry(QtCore.QRect(540, 40, 391, 200))
        self.roomWidget.setObjectName("roomWidget")

        self.label_4 = QtWidgets.QLabel(self.roomWidget)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 141, 21))
        self.label_4.setObjectName("label_4")
        self.roomLabel=QtWidgets.QLabel(self.roomWidget)
        self.roomLabel.setGeometry(QtCore.QRect(200, 80, 100, 100))
        self.roomLabel.setObjectName("roomLabel")

        ##############获取频率——spinbox############
        self.freqSpinbox = QtWidgets.QSpinBox(self.StatusDisplay)
        self.freqSpinbox.setGeometry(QtCore.QRect(550, 400, 80, 40))
        self.freqSpinbox.setObjectName("freqSpinbox")
        self.freqSpinbox.setRange(50, 100)

        self.freqButton = QtWidgets.QPushButton(self.StatusDisplay)
        self.freqButton.setGeometry(QtCore.QRect(800, 400, 112, 34))
        self.freqButton.setObjectName("freqButton")

       # self.freqButton.clicked.connect(self.freqChanged)
        ##############获取策略——RadioButton#################
        self.radioButton = QtWidgets.QRadioButton(self.StatusDisplay)
        self.radioButton.setGeometry(QtCore.QRect(540, 280, 132, 22))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.StatusDisplay)
        self.radioButton_2.setGeometry(QtCore.QRect(670, 280, 132, 22))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.StatusDisplay)
        self.radioButton_3.setGeometry(QtCore.QRect(800, 280, 132, 22))
        self.radioButton_3.setObjectName("radioButton_3")

        self.straconfButton = QtWidgets.QPushButton(self.StatusDisplay)
        self.straconfButton.setGeometry(QtCore.QRect(680, 330, 112, 34))
        self.straconfButton.setObjectName("straconfButton")

        self.showMes()

        self.straconfButton.clicked.connect(self.on_tellmeButton_clicked)

        # ################频率微调和滑块信号槽#############
        # self.freqSlider.valueChanged.connect(self.freqSpinbox.setValue)
        self.freqButton.clicked.connect(self.freqChanged)

        self.retranslateUi(self.StatusDisplay)
        QtCore.QMetaObject.connectSlotsByName(self.StatusDisplay)

    def on_tellmeButton_clicked(self):
        print("radio changed")
        if (self.radioButton.isChecked()):
            self.controller.strat=1
        if (self.radioButton_2.isChecked()):
            self.controller.strat=2
        if (self.radioButton_3.isChecked()):
            self.controller.strat=3
        self.controller.changeStrat()

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
        self.label_3.setText(_translate("StatusDisplay", "状态："))
        self.radioButton.setText(_translate("StatusDisplay", "策略一"))
        self.radioButton_2.setText(_translate("StatusDisplay", "策略二"))
        self.radioButton_3.setText(_translate("StatusDisplay", "策略三"))
        self.label_4.setText(_translate("StatusDisplay", "当前连接房间："))

    def showMes(self):
        del self.mconnec[:]
        self.controller.getFreq()
        self.controller.getStrat()
        if(self.controller.getStatu()==0):
            self.mtemp=22.0
            self.mstatus="制冷"
        else:
            self.mtemp=28.0
            self.mstatus="制热"

        self.tempLabel.setText(str(self.mtemp)+'℃')
        if self.mvelocity==0:
            self.veloLabel.setText("低速")
        elif self.mvelocity==1:
            self.veloLabel.setText("中速")
        elif self.mvelocity==2:
            self.veloLabel.setText("高速")
        self.statuLabel.setText(self.mstatus)

        list=self.controller.getConnec()
        x=0
        connecstr=""
        while x<len(list):
            connecstr+=str(list[x])
            connecstr+="\n"
            x+=1
        self.roomLabel.setText(connecstr)
        #####刷新测试
        #self.roomLabel.setNum(time.clock())

        if self.controller.strat==1:
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(False)
        elif self.controller.strat==2:
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.radioButton_3.setChecked(False)
        elif self.controller.strat==3:
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.radioButton_3.setChecked(False)

        self.freqSpinbox.setValue(self.controller.freq)


