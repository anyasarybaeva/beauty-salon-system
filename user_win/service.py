# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/service.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QListWidget,QListWidgetItem
)
import psycopg2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 740)
        MainWindow.setStyleSheet("background-color: rgb(255, 220, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 60, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(760, -10, 261, 751))
        self.label_4.setStyleSheet("background-color: rgb(251, 229, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-30, 0, 261, 751))
        self.label_5.setStyleSheet("background-color: rgb(251, 229, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 150, 531, 481))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("ui/../img/salon-2.png"))
        self.label_8.setObjectName("label_8")
        self.QlistWidget = QtWidgets.QListWidget(self.centralwidget)
        self.QlistWidget.setGeometry(QtCore.QRect(370, 240, 256, 291))
        self.QlistWidget.setStyleSheet("background-color: rgb(255, 170, 252);")
        self.QlistWidget.setObjectName("listWidget")
        self.fill_list()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 30, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Услуги"))
    def fill_list(self):
        conn = psycopg2.connect(dbname='салон красоты', user='annasarybaeva', host='localhost')
        cursor = conn.cursor()
        cursor.execute('SELECT Название,Цена FROM Услуга WHERE Статус=%s',('Активная',))
        for row in cursor:
            self.QlistWidget.addItem((row[0].lower())+" - "+str(row[1])+" руб.")
        cursor.close()
        conn.close()
        self.QlistWidget.sortItems()
class service(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
