# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_insertuser.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QMessageBox
from controller.main import M_insertUserController

class Ui_insertusr(object):
    def setupUi(self, MainWindow):
        self.insertusr=QWidget(MainWindow)
        self.insertusr.setObjectName("insertusrWidget")
        self.insertusr.resize(990, 500)
        self.insertusr.setGeometry(QtCore.QRect(30, 30, 990, 500))

        self.label = QtWidgets.QLabel(self.insertusr)
        self.label.setGeometry(QtCore.QRect(250, 120, 80, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.insertusr)
        self.label_2.setGeometry(QtCore.QRect(250, 200, 80, 20))
        self.label_2.setObjectName("label_2")

        self.nameEdit = QtWidgets.QLineEdit(self.insertusr)
        self.nameEdit.setGeometry(QtCore.QRect(360, 110, 350, 30))
        self.nameEdit.setObjectName("nameEdit")
        self.pwdEdit = QtWidgets.QLineEdit(self.insertusr)
        self.pwdEdit.setGeometry(QtCore.QRect(360, 190, 350, 30))
        self.pwdEdit.setObjectName("pwdEdit")

        self.ensureButton = QtWidgets.QPushButton(self.insertusr)
        self.ensureButton.setGeometry(QtCore.QRect(430, 300, 112, 34))
        self.ensureButton.setObjectName("ensureButton")
        self.ensureButton.clicked.connect(self.insertUser)

        self.retranslateUi(self.insertusr)
        QtCore.QMetaObject.connectSlotsByName(self.insertusr)

    def retranslateUi(self, insertusr):
        _translate = QtCore.QCoreApplication.translate
        insertusr.setWindowTitle(_translate("insertusr", "Form"))
        self.label.setText(_translate("insertusr", "用户名："))
        self.label_2.setText(_translate("insertusr", "身份证号："))
        self.ensureButton.setText(_translate("insertusr", "确认"))

    def insertUser(self):
        # 取输入的用户名与密码
        userName = self.nameEdit.text()
        passwd = self.pwdEdit.text()

        # 调用控制器的登录认证函数
        controller=M_insertUserController.InsertUserController()
        print("haha")
        message=controller.insert(userName,passwd)

        # 根据认证结果弹窗，执行下一步
        Message = QMessageBox()  # 一个消息框
        # 消息框的类型（内置了五种好像）（本体，标题，正文，按键组）
        QMessageBox.information(Message, "Message",message, QMessageBox.Ok)
        self.nameEdit.clear()
        self.pwdEdit.clear()