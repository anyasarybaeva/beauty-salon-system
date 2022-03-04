from select import select
from traceback import print_tb
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QListWidget,QListWidgetItem
)
import psycopg2
from admin_win.lk import Ui_MainWindow
from utils.utils import db
from admin_win.error import Ui_Dialog
class error(QMainWindow,Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
class lk(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.help=db()
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget_2.setSortingEnabled(True)
        self.fill_table_zanis()
        self.fill_table_material()
        self.pushButton_2.clicked.connect(self.btn_handler)
        self.pushButton.clicked.connect(self.btn_mat_handler)

    def name(self,number):
        cursor = self.help.conn.cursor()
        cursor.execute('SELECT ФИО FROM Сотрудник WHERE Код=%s',(number,))
        for row in cursor:
            self.name_label.setText(row[0]+"  личный кабинет")
        cursor.close()
    def fill_table_zanis(self):
        cursor1 = self.help.conn.cursor()
        cursor1.execute('SELECT Номер,Номер_телефона,Название_услуги,Дата ,Статус FROM Запись')
        self.tableWidget_2.setRowCount(100)
        tablerow=0
        self.dict={}
        for row in cursor1:
            self.dict[row[0]]=QtWidgets.QPushButton(self.widget)
            if row[4]=='Актуальная':
                self.dict[row[0]].setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                self.dict[row[0]].setStyleSheet("background-color: rgb(255, 0, 10);")
            self.dict[row[0]].setText(row[4])
            self.tableWidget_2.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget_2.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget_2.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget_2.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget_2.setCellWidget(tablerow,4, self.dict[row[0]])
            tablerow+=1
        cursor1.close()
    def fill_table_material(self):
        self.tableWidget.setRowCount(20)
        cursor = self.help.conn.cursor()
        cursor.execute('SELECT * FROM Материал')
        self.help.fill_table(cursor,self.tableWidget)
        cursor.close()
    def btn_handler(self):
        if self.lineEdit_2.text()=="":
            er=error(self)
            er.show()
            return
        new_stat='Архивная'
        cursor1 = self.help.conn.cursor()
        if self.dict[int(self.lineEdit_2.text())].text()=='Архивная':
            new_stat='Актуальная'
            self.dict[int(self.lineEdit_2.text())].setText("Актуальная")
            self.dict[int(self.lineEdit_2.text())].setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            new_stat='Архивная'
            self.dict[int(self.lineEdit_2.text())].setText("Архивная")
            self.dict[int(self.lineEdit_2.text())].setStyleSheet("background-color: rgb(255, 0, 10);")
        cursor1.execute("UPDATE Запись SET Статус=%s"
            "WHERE Номер = %s",
            (new_stat,int(self.lineEdit_2.text())),)
        self.help.conn.commit()
        cursor1.close()
    def btn_mat_handler(self):
        if self.lineEdit.text()=="":
            er=error(self)
            er.show()
            return
        cursor1 = self.help.conn.cursor()
