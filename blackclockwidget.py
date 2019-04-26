# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blackclockwidget.ui',
# licensing of 'blackclockwidget.ui' applies.
#
# Created: Tue Apr 23 16:51:52 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_BlackClock(object):
    def setupUi(self, BlackClock):
        BlackClock.setObjectName("BlackClock")
        BlackClock.resize(1032, 648)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BlackClock.setWindowIcon(icon)
        self.lcdNumber = QtWidgets.QLCDNumber(BlackClock)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 30, 851, 521))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(BlackClock)
        QtCore.QMetaObject.connectSlotsByName(BlackClock)

    def retranslateUi(self, BlackClock):
        BlackClock.setWindowTitle(QtWidgets.QApplication.translate("BlackClock", "Heavy-Laser", None, -1))

import resources_rc
