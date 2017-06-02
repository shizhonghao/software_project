# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox

from controller.servent.S_LoginController import S_LoginController


#这玩意一定要改
class Ui_Form(QWidget):
    #告知主窗口登录完成的信号
    _haslogged = pyqtSignal()

    def setupUi(self,parent):
        #继承在主窗口上
        self.parent = parent

        #子界面上的作画区
        self.Form = QWidget(parent) #生成在父界面上
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
        #lable_登录名
        self.label_id = QtWidgets.QLabel(self.widget)
        self.label_id.setGeometry(QtCore.QRect(0, 0, 80, 50))
        self.label_id.setStyleSheet("border-right:1px groove  rgb(255, 85, 0);")
        self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id.setObjectName("label_id")
        #input_登录名
        self.lineEdit_id = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_id.setGeometry(QtCore.QRect(80, -1, 241, 52))
        self.lineEdit_id.setStyleSheet("border-color: rgba(255, 255, 255, 0);font: 11pt 'Adobe Hebrew';")
        self.lineEdit_id.setObjectName("lineEdit")


        # 输入框-身份证号
        self.widget_2 = QtWidgets.QWidget(self.Form)
        self.widget_2.setGeometry(QtCore.QRect(60, 142, 300, 45))
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 127, 180);")
        self.widget_2.setObjectName("widget_2")
        # lable_身份证号
        self.label_card = QtWidgets.QLabel(self.widget_2)
        self.label_card.setGeometry(QtCore.QRect(0, 0, 80, 50))
        self.label_card.setStyleSheet("border-right:1px groove  rgb(255, 85, 0);")
        self.label_card.setAlignment(QtCore.Qt.AlignCenter)
        self.label_card.setObjectName("label_card")
        # input_身份证号
        self.lineEdit_card = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_card.setGeometry(QtCore.QRect(80, -1, 241, 52))
        self.lineEdit_card.setStyleSheet("border-color: rgba(255, 255, 255, 0);font: 11pt 'Adobe Hebrew'")
        self.lineEdit_card.setObjectName("lineEdit_2")

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
        self.label_id.setText(_translate("Form", "账号"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "从机用户登录"))
        self.label_card.setText(_translate("Form", "身份证号"))

    def hide(self):
        self.Form.hide()

    def show(self):
        self.Form.show()
        self.Form.raise_()

    #交互请求：登录
    def checkInp(self):
        #取输入的用户名与身份证号
        userName = self.lineEdit_id.text()
        id_card = self.lineEdit_card.text()

        #调用控制器的登录认证函数
        logincontroller = S_LoginController()
        res ,message= logincontroller.Login(userName,id_card)

        #根据认证结果弹窗，执行下一步
        Message = QMessageBox()#一个消息框
        #消息框的类型（内置了五种好像）（本体，标题，正文，按键组）
        if res == True:
            QMessageBox.information(Message,"Message", message,QMessageBox.Ok)
            self.hide()
            self._haslogged.emit()
        else:
            QMessageBox.information(Message, "Message", message, QMessageBox.Ok)
            self.lineEdit_card.clear()



