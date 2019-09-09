# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'citybus_udon1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_city_bus(object):
    def setupUi(self, city_bus):
        city_bus.setObjectName("city_bus")
        city_bus.resize(1024, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        city_bus.setFont(font)
        city_bus.setTabletTracking(True)
        city_bus.setLayoutDirection(QtCore.Qt.LeftToRight)
        city_bus.setAutoFillBackground(False)
        self.studen = QtWidgets.QPushButton(city_bus)
        self.studen.setGeometry(QtCore.QRect(70, 210, 400, 350))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.studen.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.studen.setIcon(icon)
        self.studen.setIconSize(QtCore.QSize(250, 250))
        self.studen.setObjectName("studen")
        self.people = QtWidgets.QPushButton(city_bus)
        self.people.setGeometry(QtCore.QRect(550, 210, 400, 350))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.people.setFont(font)
        self.people.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.people.setAutoFillBackground(False)
        self.people.setIcon(icon)
        self.people.setIconSize(QtCore.QSize(250, 250))
        self.people.setCheckable(False)
        self.people.setAutoExclusive(False)
        self.people.setObjectName("people")
        self.display = QtWidgets.QLCDNumber(city_bus)
        self.display.setGeometry(QtCore.QRect(270, 10, 491, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.display.setFont(font)
        self.display.setObjectName("display")

        self.retranslateUi(city_bus)
        QtCore.QMetaObject.connectSlotsByName(city_bus)

    def retranslateUi(self, city_bus):
        _translate = QtCore.QCoreApplication.translate
        city_bus.setWindowTitle(_translate("city_bus", "Form"))
        self.studen.setText(_translate("city_bus", "นักเรียน"))
        self.people.setText(_translate("city_bus", "คนทั่วไป"))

