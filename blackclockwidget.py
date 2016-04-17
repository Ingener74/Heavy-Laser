# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blackclockwidget.ui'
#
# Created: Sun Apr 17 10:50:02 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BlackClock(object):
    def setupUi(self, BlackClock):
        BlackClock.setObjectName("BlackClock")
        BlackClock.resize(1412, 1075)
        self.lcdNumber = QtGui.QLCDNumber(BlackClock)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 30, 1241, 901))
        self.lcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(BlackClock)
        QtCore.QMetaObject.connectSlotsByName(BlackClock)

    def retranslateUi(self, BlackClock):
        BlackClock.setWindowTitle(QtGui.QApplication.translate("BlackClock", "Form", None, QtGui.QApplication.UnicodeUTF8))

