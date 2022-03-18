
from keyword import softkwlist
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QListWidget,QListWidgetItem
)
from admin_win.ui_win.lk import Ui_MainWindow
from utils.utils import db
from admin_win.dialog_win.dialog_win import good,error
global n
class lk(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.help=db()
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget_2.setSortingEnabled(True)
        self.fill_table_material()
        self.pushButton_2.clicked.connect(self.btn_handler)
        self.pushButton.clicked.connect(self.btn_mat_handler)
        self.pushButton_3.clicked.connect(self.btn_ras_handler)

    def name(self,number):
        cursor = self.help.conn.cursor()
        cursor.execute('SELECT ФИО FROM Сотрудник WHERE Код=%s',(number,))
        for row in cursor:
            self.name_label.setText(row[0]+"  личный кабинет")
        self.num=number
        self.fill_table_zanis()

        cursor.close()
        
    def fill_table_zanis(self):
        cursor1 = self.help.conn.cursor()
        cursor1.execute('SELECT Номер,Номер_телефона,Название_услуги,Дата ,Статус FROM Запись WHERE Код_сотрудника=%s',(int(self.num),))
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

    def btn_handler(self):#not working
        if self.lineEdit_2.text()=="":
            er=error(self)
            er.show()
            return
        cursor1 = self.help.conn.cursor()
        if self.dict[int(self.lineEdit_2.text())].text()=='Актуальная':
            try:
                cursor1.execute("UPDATE Запись SET Статус=%s"
                "WHERE Номер = %s",
                ("Архивная",int(self.lineEdit_2.text())),)
                self.help.conn.commit()
                cursor1.close()
                self.dict[int(self.lineEdit_2.text())].setText("Архивная")
                self.dict[int(self.lineEdit_2.text())].setStyleSheet("background-color: rgb(255, 0, 10);")    
            except:
                er=error(self)
                er.label_2.setText("Данные")
                er.show()

    def btn_mat_handler(self):
            
        cursor = self.help.conn.cursor()
        if self.lineEdit.text()=="":
            cursor.execute('SELECT * FROM Материал')
            self.tableWidget.clearContents()
            self.help.fill_table(cursor,self.tableWidget)
            return
        try:
            cursor.execute('SELECT * FROM Материал WHERE Название like %s',(self.lineEdit.text()+'%',))
            self.tableWidget.clearContents()
            self.help.fill_table(cursor,self.tableWidget)
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()
        cursor.close()

    def btn_ras_handler(self):
        if self.lineEdit_col.text()=="" or self.lineEdit_mat.text()=="" or self.lineEdit_numb.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()
            cursor.execute("UPDATE Материал SET Количество=Количество-%s" 
            "WHERE Название=%s",(int(self.lineEdit_col.text()),self.lineEdit_mat.text(),))
            cursor.execute('INSERT INTO Расход(Номер_записи,Название,Количество) VALUES(%s,%s,%s)',(int(self.lineEdit_numb.text()),self.lineEdit_mat.text(),int(self.lineEdit_col.text()),))
            self.help.conn.commit()
            self.tableWidget.clearContents()
            self.fill_table_material()
            er=good(self)
            cursor.close()
            er.show()
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()