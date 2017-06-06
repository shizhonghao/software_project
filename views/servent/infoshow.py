# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoshow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#数据类
from views.servent.figure import Figure_Canvas
from controller.servent.SBoardControl import S_BoardController
from  datetime  import  *


class Ui_S_Board(QtWidgets.QWidget):
    start = QtCore.pyqtSignal()
    def setupUi(self, parent,servent):
        self.S_Board = QtWidgets.QWidget(parent) #生成在父界面上
        self.S_Board.setObjectName("S_Board")
        self.S_Board.resize(600, 450)
        self.S_Board.setGeometry(QtCore.QRect(0,30,600,450))  #展示窗口定位


        self.windshow = QtWidgets.QComboBox(self.S_Board)
        self.windshow.setGeometry(QtCore.QRect(70, 0, 69, 22))
        self.windshow.setObjectName("windshow")
        self.windshow.addItem("")
        self.windshow.addItem("")
        self.windshow.addItem("")
        self.windlabel = QtWidgets.QLabel(self.S_Board)
        self.windlabel.setGeometry(QtCore.QRect(10, 0, 54, 21))
        self.windlabel.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.windlabel.setObjectName("windlabel")
        self.dtlabel = QtWidgets.QLabel(self.S_Board)
        self.dtlabel.setGeometry(QtCore.QRect(200, 0, 54, 21))
        self.dtlabel.setObjectName("dtlabel")
        self.dtshow_cold = QtWidgets.QComboBox(self.S_Board)
        self.dtshow_cold.setGeometry(QtCore.QRect(270, 0, 69, 22))
        self.dtshow_cold.setObjectName("dtshow_hot")
        self.dtshow_cold.addItem("")
        self.dtshow_cold.addItem("")
        self.dtshow_cold.addItem("")
        self.dtshow_cold.addItem("")
        self.dtshow_cold.addItem("")
        self.dtshow_cold.addItem("")
        self.dtshow_cold.addItem("")
        self.rtlabel = QtWidgets.QLabel(self.S_Board)
        self.rtlabel.setGeometry(QtCore.QRect(200, 40, 54, 12))
        self.rtlabel.setObjectName("rtlabel")
        self.rtshow = QtWidgets.QLabel(self.S_Board)
        self.rtshow.setGeometry(QtCore.QRect(270, 35, 71, 21))
        self.rtshow.setObjectName("rtshow")
        self.dtshow_hot = QtWidgets.QComboBox(self.S_Board)
        self.dtshow_hot.setGeometry(QtCore.QRect(270, 0, 69, 22))
        self.dtshow_hot.setObjectName("dtshow_cold")
        self.dtshow_hot.addItem("")
        self.dtshow_hot.addItem("")
        self.dtshow_hot.addItem("")
        self.dtshow_hot.addItem("")
        self.dtshow_hot.addItem("")
        self.dtshow_hot.addItem("")
        self.modellabel = QtWidgets.QLabel(self.S_Board)
        self.modellabel.setGeometry(QtCore.QRect(20, 30, 31, 31))
        self.modellabel.setObjectName("modellabel")
        self.modelshow = QtWidgets.QLabel(self.S_Board)
        self.modelshow.setGeometry(QtCore.QRect(70, 36, 71, 20))
        self.modelshow.setObjectName("modelshow")

        self.gridLayoutWidget = QtWidgets.QWidget(self.S_Board)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 60, 600, 390))  # 定义gridLayout控件的大小和位置，4个数字分别为左边坐标，上边坐标，长，宽
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        # 在gridLayoutWidget 上创建一个网格Layout，注意以gridLayoutWidget为参
        self.gridLayout_2.setObjectName("gridLayout_2")
        # ===通过graphicview来显示图形
        self.graphicview = QtWidgets.QGraphicsView(self.S_Board)
        # 第一步，创建一个QGraphicsView，注意同样以gridLayoutWidget为参
        self.graphicview.setObjectName("graphicview")
        self.gridLayout_2.addWidget(self.graphicview, 0, 0)
        #第二步，将该QGraphicsView放入Layout中

        self.dr = Figure_Canvas()
        #实例化一个FigureCanvas
        self.graphicscene = QtWidgets.QGraphicsScene()
        # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphicscene.addWidget(self.dr)
        # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.graphicview.setScene(self.graphicscene)
        # 第五步，把QGraphicsScene放入QGraphicsView
        self.graphicview.show()
        # 最后，调用show方法呈现图形

        self.controller = S_BoardController()


        self.retranslateUi(self.S_Board)
        QtCore.QMetaObject.connectSlotsByName(self.S_Board)

        # 刷新定时器
        self.timer =QtCore.QTimer()
        self.timer.setInterval(1000)

        #信号与槽连接
        self.timer.timeout.connect(self.painting)
        self.windshow.currentIndexChanged.connect(self.wind_change)
        self.dtshow_hot.currentIndexChanged.connect(self.t_raise)
        self.dtshow_cold.currentIndexChanged.connect(self.t_raise)

        self.roomNo = 826
        self.targetT = 27
        self.targetW = 1
        self.sysT = 30
        self.sysW = 1
        self.sysModel = 0
        self.loggedOn = datetime.strptime("2017-06-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        self.eng_cost = 0.00
        self.money_cost = 0.00
        self.start_blowing = 0

        self.wpre = datetime.now()
        self.tptr = datetime.now()


    def retranslateUi(self, S_Board):
        _translate = QtCore.QCoreApplication.translate
        S_Board.setWindowTitle(_translate("S_Board", "Form"))
        self.windshow.setItemText(0, _translate("S_Board", "high"))
        self.windshow.setItemText(1, _translate("S_Board", "mid"))
        self.windshow.setItemText(2, _translate("S_Board", "low"))
        self.windlabel.setText(_translate("S_Board", "风速"))
        self.dtlabel.setText(_translate("S_Board", "目标温度"))
        self.dtshow_cold.setItemText(0, _translate("S_Board", "24℃"))
        self.dtshow_cold.setItemText(1, _translate("S_Board", "23℃"))
        self.dtshow_cold.setItemText(2, _translate("S_Board", "22℃"))
        self.dtshow_cold.setItemText(3, _translate("S_Board", "21℃"))
        self.dtshow_cold.setItemText(4, _translate("S_Board", "20℃"))
        self.dtshow_cold.setItemText(5, _translate("S_Board", "19℃"))
        self.dtshow_cold.setItemText(6, _translate("S_Board", "18℃"))
        self.rtlabel.setText(_translate("S_Board", "实际温度"))
        self.rtshow.setText(_translate("S_Board", "29度"))
        self.dtshow_hot.setItemText(0, _translate("S_Board", "30℃"))
        self.dtshow_hot.setItemText(1, _translate("S_Board", "29℃"))
        self.dtshow_hot.setItemText(2, _translate("S_Board", "28℃"))
        self.dtshow_hot.setItemText(3, _translate("S_Board", "27℃"))
        self.dtshow_hot.setItemText(4, _translate("S_Board", "26℃"))
        self.dtshow_hot.setItemText(5, _translate("S_Board", "25℃"))
        self.modellabel.setText(_translate("S_Board", "模式"))
        self.modelshow.setText(_translate("S_Board", "制冷"))

    def hide(self):
        self.S_Board.hide()

    def show(self):
        #raise函数？？？？？
        self.S_Board.show()
        if(self.sysModel == 0):
            self.dtshow_cold.show()
            self.dtshow_hot.hide()
            self.modelshow.setText("制冷")
        else:
            self.dtshow_hot.show()
            self.dtshow_cold.hide()
            self.modelshow.setText("供暖")
        #self.timer.start()
        self.cnt=0; #temppppppppp

    def painting(self):
        if(self.cnt % 2 == 0):
            self.dr.test(24,30)
            self.rtshow.setText("24度")
            self.cnt = self.cnt + 1
        else:
            self.dr.test(26,30)
            self.rtshow.setText("26度")
            self.cnt = self.cnt + 1

    def wind_change(self):
        now = datetime.now() #信息发送处理
        #if((int)(now - self.wpre).seconds >= 1):
        print("into")
        self.controller.Wind_Change(self.windshow.currentData())


    def t_raise(self):
        print("into")
        self.controller.T_raise(self.windshow.currentData())

    def getCurrentState(self):
        self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing = self.controller.getCurrentState()
        return self.roomNo, self.targetT, self.targetW, self.sysT, self.sysW, self.sysModel, self.loggedOn, self.eng_cost, self.money_cost, self.start_blowing

