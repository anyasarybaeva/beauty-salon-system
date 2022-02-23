# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from master_window import MasterWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 757)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 192, 249);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 110, 791, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setFamily("Courier New")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color:rgb(10, 0, 0)")
        self.btn_master = QtWidgets.QPushButton(self.centralwidget)
        self.btn_master.setGeometry(QtCore.QRect(400, 170, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.btn_master.setFont(font)
        self.btn_master.setObjectName("btn_master")
        self.btn_services = QtWidgets.QPushButton(self.centralwidget)
        self.btn_services.setGeometry(QtCore.QRect(200, 170, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.btn_services.setFont(font)
        self.btn_services.setObjectName("btn_services")
        self.btn_services_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_services_2.setGeometry(QtCore.QRect(600, 170, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.btn_services_2.setFont(font)
        self.btn_services_2.setObjectName("btn_services_2")
        self.btn_services_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_services_3.setGeometry(QtCore.QRect(0, 170, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.btn_services_3.setFont(font)
        self.btn_services_3.setObjectName("btn_services_3")
        self.labe_image = QtWidgets.QLabel(self.centralwidget)
        self.labe_image.setGeometry(QtCore.QRect(0, 219, 800, 241))
        self.labe_image.setStyleSheet("background-image: url(./img/salony-krasoty.jpg);\n""background-color: rgb(255, 255, 255);")
        self.labe_image.setText("")
        self.labe_image.setObjectName("labe_image")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 560, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.buttons_handlers()#handelrs 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cалон красоты"))
        self.label.setText(_translate("MainWindow", "                 Салон красоты"))
        self.btn_master.setText(_translate("MainWindow", "Мастера"))
        self.btn_services.setText(_translate("MainWindow", "Услуги"))
        self.btn_services_2.setText(_translate("MainWindow", "Работы"))
        self.btn_services_3.setText(_translate("MainWindow", "О нас"))
        self.label_2.setText(_translate("MainWindow", "Контакты\nтел. 869629372768\nэл.почта: anya.sarybaeva@mail.ru\nадресс: г. Москва ул. Смольная д.5"))
   
    def buttons_handlers(self):#method for handlers need fixing
        self.btn_master.clicked.connect(self.open_master_win)
        self.btn_services.clicked.connect(self.open_master_win)
        self.btn_services_2.clicked.connect(self.open_examples_win)
        self.btn_services_3.clicked.connect(self.open_master_win)
    #handlers
    def open_master_win(self):
        self.newWin = MasterWindow(self)
        self.hide()
        self.newWin.show()
    def open_examples_win(self):
        self.newWin = MasterWindow(self)#change
        self.hide()
        self.newWin.show()        
