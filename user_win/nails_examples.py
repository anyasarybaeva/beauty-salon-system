# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/nails_example.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 740)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 252);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 60, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 50, 251, 191))
        self.label_2.setStyleSheet("background-color: rgb(255, 91, 34);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ui/../img/nails-2.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 320, 111, 141))
        self.label_3.setStyleSheet("background-color: rgb(255, 91, 34);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ui/../img/nails1-2.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 0, 261, 751))
        self.label_4.setStyleSheet("background-color: rgb(251, 229, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 261, 751))
        self.label_5.setStyleSheet("background-color: rgb(251, 229, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 510, 151, 191))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("ui/../img/nails2-2.png"))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class nails_examples(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)