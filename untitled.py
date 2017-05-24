# -*- coding: utf-8 -*-

# self.Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_Form(object):
    #这个函数原来的传参不是这样的，一定要把父窗口(这里是MainWindow）传进来
    def setupUi(self,MainWindow):
        #子界面上的作画区
        self.Form = QWidget(MainWindow) #生成在父界面上
        self.Form.setObjectName("Form")
        self.Form.resize(400, 300)
        self.Form.setStyleSheet("background-color: rgb(28, 62, 255);")
        self.Form.setGeometry(QtCore.QRect(140, 240, 400, 300))

        self.label = QtWidgets.QLabel(self.Form)#生成在子界面上
        self.label.setGeometry(QtCore.QRect(90, 60, 231, 91))
        self.label.setObjectName("label")
        _translate = QtCore.QCoreApplication.translate
        self.label.setText("this is a subwidgt")

        self.pushButton = QtWidgets.QPushButton(self.Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 240, 112, 34))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton2")
        self.pushButton.clicked.connect(self.Form.hide)
        self.pushButton.setText("close")

    def hide(self):
        self.Form.hide()

    def show(self):
        self.Form.show()
        self.Form.raise_()


