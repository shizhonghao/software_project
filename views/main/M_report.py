# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_report.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_Report(object):
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

    def retranslateUi(self, Report):
        _translate = QtCore.QCoreApplication.translate
        Report.setWindowTitle(_translate("Report", "Form"))
        self.labeltest2.setText(_translate("Report", "报表界面"))

