from locale import currency
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, date, time
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from admin_win.ui_win.lk_admin import Ui_MainWindow
from utils.utils import db
from admin_win.dialog_win.dialog_win import good,error

class lk_admin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.help=db()

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget_2.setSortingEnabled(True)
        
        #matherial
        self.fill_table_mat()
        self.pushButton.clicked.connect(self.btn_find)
        self.pushButton_3.clicked.connect(self.btn_enter_ras)
        self.pushButton_8.clicked.connect(self.btn_enter_mat)
        self.pushButton_13.clicked.connect(self.btn_ch_mat)

        #client
        self.fill_table_cliente()
        self.pushButton_7.clicked.connect(self.btn_enter_client)

        #sortudnic 
        self.fill_table_master()
        self.pushButton_delete_2.clicked.connect(self.btn_find_mast)
        self.pushButton_delete_3.clicked.connect(self.btn_change_mast)
        self.pushButton_delete.clicked.connect(self.btn_del_mast)
        self.pushButton_delete_4.clicked.connect(self.btn_insr_mast)
        #service

        self.fill_table_service()
        self.pushButton_delete_6.clicked.connect(self.btn_find_serv)
        self.pushButton_delete_5.clicked.connect(self.btn_change_stat_serv)
        self.pushButton_delete_7.clicked.connect(self.btn_add_serv)
        self.pushButton_delete_8.clicked.connect(self.btn_change_price_serv)

        #zanis
        self.fill_table_zapis()
        self.pushButton_9.clicked.connect(self.btn_find_zap)
        self.pushButton_2.clicked.connect(self.btn_change_stat_zap)
        self.pushButton_10.clicked.connect(self.btn_change_date_zap)
        self.pushButton_11.clicked.connect(self.btn_cancel_zap)
        self.pushButton_12.clicked.connect(self.btn_add_zap)

    #need test
    #matherial
    def btn_find(self):
        cursor = self.help.conn.cursor()
        if self.lineEdit.text()=="":
            cursor.execute('SELECT * FROM Материал')
            self.tableWidget.clearContents()
            self.help.fill_table(cursor,self.tableWidget)
        try:
            cursor.execute('SELECT * FROM Материал WHERE Название like %s',(self.lineEdit.text()+'%',))
            self.tableWidget.clearContents()
            self.help.fill_table(cursor,self.tableWidget)
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Нет совпаденией")
            er.show()
    
    def btn_enter_ras(self):
        self.help=db()
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
            cursor.execute('SELECT * FROM Материал')
            self.help.fill_table(cursor,self.tableWidget)            
            er=good(self)
            cursor.close()
        except :
            er=error(self)
            er.label_2.setText("Данные")
        er.show()
    
    def btn_enter_mat(self):
        self.help=db()
        if self.lineEdit_mat_6.text()=="" or self.lineEdit_numb_4.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()
            cursor.execute('INSERT INTO Материал(Название,Количество) VALUES(%s,%s)',(self.lineEdit_mat_6.text(),int(self.lineEdit_numb_4.text()),))
            self.help.conn.commit()
            self.tableWidget.clearContents()
            cursor.execute('SELECT * FROM Материал')
            self.help.fill_table(cursor,self.tableWidget)            
            cursor.close()
            er=good(self)
        except :
            er=error(self)
            er.label_2.setText("Данные")            
        er.show()

    def fill_table_mat(self):
        cursor = self.help.conn.cursor()
        self.tableWidget.setRowCount(20)
        cursor.execute('SELECT * FROM Материал')
        self.help.fill_table(cursor,self.tableWidget)
        cursor.close()

    def btn_ch_mat(self):
        if self.lineEdit_mat_6.text()=="" or self.lineEdit_numb_4.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()
            cursor.execute("UPDATE Материал SET Количество=Количество+%s" 
            "WHERE Название=%s",(int(self.lineEdit_numb_4.text()),self.lineEdit_mat_6.text(),))
            self.help.conn.commit()
            self.tableWidget.clearContents()
            cursor.execute('SELECT * FROM Материал')
            self.help.fill_table(cursor,self.tableWidget)            
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")            
            er.show()
    #client done
    
    def fill_table_cliente(self):
        cursor = self.help.conn.cursor()
        self.tableWidget_3.setRowCount(20)
        cursor.execute('SELECT * FROM Клиент')
        self.help.fill_table(cursor,self.tableWidget_3)
        cursor.close()

    def btn_enter_client(self):
        if self.lineEdit_mat_3.text()=="" or self.lineEdit_mat_4.text()=="" or self.lineEdit_mat_5.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor1 = self.help.conn.cursor()
            cursor1.execute('INSERT INTO Клиент VALUES(%s,%s,%s)',(self.lineEdit_mat_3.text(),self.lineEdit_mat_4.text(),self.lineEdit_mat_5.text(),))
            self.help.conn.commit()
            er=good(self)
            self.tableWidget_3.clearContents()
            cursor1.execute('SELECT * FROM Клиент')
            self.help.fill_table(cursor1,self.tableWidget_3)            
            cursor1.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
        er.show()
    #master need test
    def fill_table_master(self):#work
        cursor = self.help.conn.cursor()
        self.tableWidget_7.setRowCount(20)
        cursor.execute('SELECT * FROM Сотрудник')
        self.help.fill_table(cursor,self.tableWidget_7)
        cursor.close()
    
    def btn_find_mast(self):#work
        if self.lineEdit_mat_18.text()=="":
            self.tableWidget_7.clearContents()
            self.fill_table_master()
            return
        try:
            cursor1 = self.help.conn.cursor()
            cursor1.execute('SELECT * FROM Сотрудник WHERE ФИО=%s',(self.lineEdit_mat_18.text(),))
            self.tableWidget_7.clearContents()
            self.help.fill_table(cursor1,self.tableWidget_7)
            cursor1.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()

    def btn_change_mast(self):#test
        if self.lineEdit_mat_8.text()=="" and self.lineEdit_mat_9.text()=="" and  self.lineEdit_mat_11.text()=="" and self.lineEdit_mat_10.text()=="" :
            er=error(self)
            er.show()
            return
        if self.lineEdit_mat_8.text()=="":
            er=error(self)
            er.show()
            return
        try:
            if self.lineEdit_mat_9.text()!="":
                cursor1 = self.help.conn.cursor()
                cursor1.execute("UPDATE Сотрудник SET Номер_телефона=%s" 
                "WHERE Код=%s",(self.lineEdit_mat_9.text(),int(self.lineEdit_mat_8.text()),))
                cursor1.close()
            if self.lineEdit_mat_10.text()!="":
                cursor1 = self.help.conn.cursor()
                cursor1.execute("UPDATE Сотрудник SET Статус=%s" 
                "WHERE Код=%s",(self.lineEdit_mat_10.text(),int(self.lineEdit_mat_8.text()),))
                cursor1.close()
            if self.lineEdit_mat_11.text()!="":
                cursor1 = self.help.conn.cursor()
                cursor1.execute("UPDATE Сотрудник SET ФИО=%s" 
                "WHERE Код=%s",(self.lineEdit_mat_11.text(),int(self.lineEdit_mat_8.text()),))
                cursor1.close()
                er=good(self)
                self.tableWidget_7.clearContents()
                cursor1.execute('SELECT * FROM Сотрудник')
                self.help.fill_table(cursor1,self.tableWidget_7)
        except:
            er=error(self)
            er.label_2.setText("Данные")
        er.show()

    def btn_del_mast(self):#test 
        if self.lineEdit_mat_7.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()
            cursor.execute('DELETE FROM Сотрудник WHERE Код=%s',(int(self.lineEdit_mat_7.text()),))
            self.help.conn.commit()
            er=good(self)
            self.tableWidget_7.clearContents()
            cursor.execute('SELECT * FROM Сотрудник')
            self.help.fill_table(cursor,self.tableWidget_7)
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
            
        er.show()
        
    def btn_insr_mast(self):#test
        if self.lineEdit_mat_8.text()=="" or self.lineEdit_mat_9.text()=="" or self.lineEdit_mat_11.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()
            cursor.execute('INSERT INTO Сотрудник(Код,Номер_телефона,ФИО) VALUES(%s,%s,%s)',(int(self.lineEdit_mat_8.text()),self.lineEdit_mat_9.text(),self.lineEdit_mat_11.text(),))
            er=good(self)
            self.help.conn.commit()
            self.tableWidget_7.clearContents()
            cursor.execute('SELECT * FROM Сотрудник')
            self.help.fill_table(cursor,self.tableWidget_7)
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
        er.show()
#service
    def fill_table_service(self):
        cursor1 = self.help.conn.cursor()
        self.tableWidget_8.setRowCount(20)
        cursor1.execute('SELECT * FROM Услуга')
        tablerow=0
        self.dict_ser={}
        for row in cursor1:
            self.dict_ser[row[0]]=row[2]
            self.tableWidget_8.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget_8.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget_8.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget_8.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow+=1
        cursor1.close()

    def btn_find_serv(self):
        cursor = self.help.conn.cursor()
        if self.lineEdit_mat_14.text()=="":
            cursor.execute('SELECT * FROM Услуга')
            self.tableWidget_8.clearContents()
            self.help.fill_table(cursor,self.tableWidget_8)
        try:
            cursor.execute('SELECT * FROM Услуга WHERE Название like %s',(self.lineEdit_mat_14.text()+'%',))
            self.tableWidget_8.clearContents()
            self.help.fill_table(cursor,self.tableWidget_8)
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()
        cursor.close()

    def btn_change_stat_serv(self):
        self.help=db()
        if self.lineEdit_mat_12.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()
            if self.dict_ser[self.lineEdit_mat_12.text()]=='Архивная':
                new_stat='Активная'
            else:
                new_stat='Архивная'
            cursor.execute("UPDATE Услуга SET Статус=%s"
                "WHERE Название = %s",
                (new_stat,self.lineEdit_mat_12.text()),)
            self.help.conn.commit()
            self.tableWidget_8.clearContents()
            self.fill_table_service()
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()

    def btn_change_price_serv(self):
        self.help=db()
        if self.lineEdit_mat_19.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()
            cursor.execute("UPDATE Услуга SET Цена=%s"
                "WHERE Название = %s",
                (int(self.lineEdit_mat_19.text()),self.lineEdit_mat_12.text()),)
            self.help.conn.commit()
            self.tableWidget_8.clearContents()
            cursor.execute('SELECT * FROM Услуга')
            self.tableWidget_8.clearContents()
            self.help.fill_table(cursor,self.tableWidget_8)
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()
        cursor.close()

        
    def btn_add_serv(self):#good
        self.help=db()
        if self.lineEdit_mat_13.text()=="" or self.lineEdit_mat_17.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()
            cursor.execute('INSERT INTO Услуга(Название,Цена) VALUES(%s,%s)',(self.lineEdit_mat_13.text(),int(self.lineEdit_mat_17.text()),))
            self.help.conn.commit()
            self.tableWidget_8.clearContents()
            self.dict_ser[self.lineEdit_mat_13.text()]='Активная'
            cursor.execute('SELECT * FROM Услуга')
            self.help.fill_table(cursor,self.tableWidget_8)            
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()
        cursor.close()

    
    #zapis
    def fill_table_zapis(self):
        cursor = self.help.conn.cursor()
        self.tableWidget_2.setRowCount(50)

        cursor.execute('SELECT * FROM Запись')
        self.help.fill_table(cursor,self.tableWidget_2)
        cursor.close()

    def btn_find_zap(self):
        self.help=db()
        cursor = self.help.conn.cursor()
        if self.lineEdit_5.text()=="":
            self.tableWidget_2.clearContents()
            cursor.execute('SELECT * FROM Запись',)
            #self.fill_table_zapis()
            self.help.fill_table(cursor,self.tableWidget_2)
            cursor.close()
            return
        try:
            cursor.execute('SELECT * FROM Запись WHERE Код_сотрудника=%s',(int(self.lineEdit_5.text()),))
            self.tableWidget_2.clearContents()
            self.help.fill_table(cursor,self.tableWidget_2)
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()
        cursor.close()

    def btn_change_stat_zap(self):
        if self.lineEdit_2.text()=="":
            er=error(self)
            er.show()
            return
        cursor = self.help.conn.cursor()
        try:
            cursor.execute("UPDATE Запись SET Статус = %s"
                "WHERE Номер=%s",
                ("Архивная",int(self.lineEdit_2.text()),),)
            self.help.conn.commit()
            self.tableWidget_2.clearContents()
            cursor.execute('SELECT * FROM Запись',)
            self.help.fill_table(cursor,self.tableWidget_2)
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()
    
    def btn_change_date_zap(self):
        if self.lineEdit_2.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()

            cursor.execute("UPDATE Запись SET Дата = %s"
                "WHERE Номер=%s",
                (self.lineEdit_10.text(),int(self.lineEdit_2.text()),),)
            self.help.conn.commit()
            self.tableWidget_2.clearContents()
            cursor.execute('SELECT * FROM Запись',)
            self.help.fill_table(cursor,self.tableWidget_2)
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
            er.show()
    
    def btn_cancel_zap(self):#test after full table
        if self.lineEdit_2.text()=="":
            er=error(self)
            er.show()
            return
        try:
            cursor = self.help.conn.cursor()
            cursor.execute('DELETE FROM Запись WHERE Номер=%s',(int(self.lineEdit_2.text()),))
            self.help.conn.commit()
            er=good(self)
            self.tableWidget_2.clearContents()
            cursor.execute('SELECT * FROM Запись',)
            self.help.fill_table(cursor,self.tableWidget_2)
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
        er.show()

    def btn_add_zap(self):
        if self.lineEdit_7.text()=="" or self.lineEdit_8.text()=="" or self.lineEdit_9.text()=="":
            er=error(self)
            er.show()
            return
        num=0
        try:
            cursor = self.help.conn.cursor()
            cursor.execute('SELECT MAX(Номер) FROM Запись')
            for row in cursor:
                num=row[0]
            cursor.execute("SELECT * FROM Сотрудник WHERE Статус='работает' and Код=%s",(int(self.lineEdit_8.text()),))
            if len(cursor.fetchall())==0: 
                er=error(self)
                er.label_2.setText("Сотрудник")
                er.show()
                return
            cursor.execute("SELECT * FROM Услуга WHERE Статус='Активная' and Название=%s",(self.lineEdit_9.text(),))
            if len(cursor.fetchall())==0: 
                er=error(self)
                er.label_2.setText("Услуга")
                er.show()
                return
            cursor.execute("SELECT * FROM Клиент WHERE Номер_телефона=%s",(self.lineEdit_7.text(),))
            if len(cursor.fetchall())==0: 
                er=error(self)
                er.label_2.setText('Клиент')
                er.show()
                return
            cursor.execute('INSERT INTO Запись(Номер,Номер_телефона,Код_сотрудника,Название_услуги,Дата) VALUES(%s,%s,%s,%s,%s)',(int(num)+1,self.lineEdit_7.text(),int(self.lineEdit_8.text()),self.lineEdit_9.text(),self.lineEdit_11.text(),))
            self.help.conn.commit()
            er=good(self)
            self.tableWidget_2.clearContents()
            cursor.execute('SELECT * FROM Запись',)
            self.help.fill_table(cursor,self.tableWidget_2)
            cursor.close()
        except:
            er=error(self)
            er.label_2.setText("Данные")
        er.show()