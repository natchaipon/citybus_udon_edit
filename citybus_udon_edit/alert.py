# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alert.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_alert(object):
    def setupUi(self, alert):
        alert.setObjectName("alert")
        alert.resize(400, 112)
        alert.move(312 , 300)
        self.label = QtWidgets.QLabel(alert)
        self.label.setGeometry(QtCore.QRect(120, 40, 151, 21))
        self.label.setObjectName("label")

        self.retranslateUi(alert)
        QtCore.QMetaObject.connectSlotsByName(alert)

    def retranslateUi(self, alert):
        _translate = QtCore.QCoreApplication.translate
        alert.setWindowTitle(_translate("alert", "CityBus Udontrani"))
        self.label.setText(_translate("alert", "ชำระค่าบริกการสำเร็จ"))
