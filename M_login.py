# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QMessageBox

class Ui_Form(object):
    def setupUi(self,MainWindow):
        self.parent = MainWindow

        #子界面上的作画区
        self.Form = QWidget(MainWindow) #生成在父界面上
        self.Form.setGeometry(QtCore.QRect(140, 240, 400, 250))
        self.Form.setObjectName("Form")
        self.Form.resize(400, 250)
        self.Form.setStyleSheet("background-color: rgba(255, 170, 0, 190);")

        #标题栏
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(60, 18, 301, 41))
        self.label.setStyleSheet("border-bottom:1px groove  rgb(255, 85, 0);background-color: rgb(255, 255, 255,160);")
        self.label.setObjectName("label")

        #输入框-登录名
        self.widget = QtWidgets.QWidget(self.Form)
        self.widget.setGeometry(QtCore.QRect(60, 77, 300, 45))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 127, 180);")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.label_2.setStyleSheet("border-right:1px groove  rgb(255, 85, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.linEdit = QtWidgets.QLineEdit(self.widget)
        self.linEdit.setGeometry(QtCore.QRect(60, -1, 241, 52))
        self.linEdit.setStyleSheet("border-color: rgba(255, 255, 255, 0);font: 11pt 'Adobe Hebrew';")
        self.linEdit.setObjectName("lineEdit")

        #输入框-密码
        self.widget_2 = QtWidgets.QWidget(self.Form)
        self.widget_2.setGeometry(QtCore.QRect(60, 142, 300, 45))
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 127, 180);")
        self.widget_2.setObjectName("widget_2")

        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.label_3.setStyleSheet("border-right:1px groove  rgb(255, 85, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.linEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.linEdit_2.setGeometry(QtCore.QRect(60, -1, 241, 52))
        self.linEdit_2.setStyleSheet("border-color: rgba(255, 255, 255, 0);font: 11pt 'Adobe Hebrew'")
        self.linEdit_2.setObjectName("lineEdit_2")

        #登录按钮
        self.pushButton = QtWidgets.QPushButton(self.Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 198, 110, 34))
        #self.pushButton.setStyleSheet("border-radius:10px;background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.checkInp)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "账号"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "管理员登录"))
        self.label_3.setText(_translate("Form", "密码"))

    def hide(self):
        self.Form.hide()

    def show(self):
        self.Form.show()
        self.Form.raise_()

    def checkInp(self):

        userName = self.linEdit.text()
        passwd = self.linEdit_2.text()

        Message = QMessageBox()#一个消息框
        #消息框的类型（内置了五种好像）（本体，标题，正文，按键组）
        button = QMessageBox.question(Message,"Message", "输入的用户名为"+self.linEdit.text(),QMessageBox.Ok| QMessageBox.Cancel)
        #根据按键处理结果
        if button == QMessageBox.Ok:
            self.hide()
        else:
            return


