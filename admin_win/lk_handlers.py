
from keyword import softkwlist
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QListWidget,QListWidgetItem
)
from admin_win.ui_win.lk import Ui_MainWindow
from utils.utils import db
from admin_win.dialog_win.dialog_win import good,error
import pandas as pd

class lk(QMainWindow, Ui_MainWindow):
    def __init__(self,num, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.help=db()
        self.error=error(self)
        self.success=good(self)
        self.fill_table_material()

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget_2.setSortingEnabled(True)
      
        self.pushButton_2.clicked.connect(self.btn_appointment)
        self.pushButton.clicked.connect(self.btn_material)
        self.pushButton_3.clicked.connect(self.btn_usage)

    def name(self,number):
        cursor = self.help.conn.cursor()
        cursor.execute('SELECT ФИО FROM Сотрудник WHERE Код=%s',(number,))
        name=cursor.fetchone()
        self.name_label.setText(name[0]+"  личный кабинет")
        self.num=number
        self.fill_table_appointment()
        cursor.close()
        
    def fill_table_appointment(self):
        sql=('SELECT Номер,Номер_телефона,Название_услуги,Дата ,Статус FROM Запись WHERE Код_сотрудника=%s')
        self.zapis_df=pd.read_sql(sql, self.help.conn,params=[self.num])
        self.tableWidget_2.setRowCount(100)

        tablerow=0
        self.help.fill_table(self.zapis_df.values.tolist(),self.tableWidget_2)
        for row in self.zapis_df.values.tolist():
            if  row[4]=='Актуальная':
                self.tableWidget_2.item(tablerow,4).setBackground(QtGui.QColor(0,255,0))
            else:
                self.tableWidget_2.item(tablerow,4).setBackground(QtGui.QColor(255,0,0))
            tablerow+=1

    def fill_table_material(self):
        self.tableWidget.setRowCount(20)
        cursor = self.help.conn.cursor()
        cursor.execute('SELECT * FROM Материал')
        self.help.fill_table(cursor,self.tableWidget)
        cursor.close()

    def btn_appointment(self):
        if self.lineEdit_2.text()=="":
            self.error.label_2.setText("Пустое поле")
            self.error.show()
            return
        number=int(self.lineEdit_2.text())
        if self.zapis_df[(self.zapis_df.Номер==number)& (self.zapis_df.Статус=='Архивная')].empty:
            try:
                cursor = self.help.conn.cursor()
                cursor.execute("UPDATE Запись SET Статус=%s"
                "WHERE Номер = %s",
                ("Архивная",number),)
                self.help.conn.commit()
                cursor.close()
                self.zapis_df.loc[self.zapis_df.Номер==number,'Статус']='Архивная'                               
                self.tableWidget_2.item(self.zapis_df.loc[self.zapis_df['Номер']==number].index[0],4).setBackground(QtGui.QColor(255,0,0))
            except:
                self.error.label_2.setText("Данные")
                self.error.show()

    def btn_material(self):   
        if self.lineEdit.text()=="":
            cursor = self.help.conn.cursor()
            cursor.execute('SELECT * FROM Материал')
            self.tableWidget.clearContents()
            self.help.fill_table(cursor,self.tableWidget)
            cursor.close()
            return  
        try:
            cursor = self.help.conn.cursor()
            cursor.execute('SELECT * FROM Материал WHERE Название like %s',(self.lineEdit.text()+'%',))
            self.tableWidget.clearContents()
            self.help.fill_table(cursor,self.tableWidget)
            cursor.close()
        except:
            self.error.label_2.setText("Данные")
            self.error.show()

    def btn_usage(self):
        if self.lineEdit_col.text()=="" or self.lineEdit_mat.text()=="" or self.lineEdit_numb.text()=="":
            self.error.label_2.setText("Пустое поле")
            self.error.show()
            return
        try:
            cursor = self.help.conn.cursor()
            cursor.execute("UPDATE Материал SET Количество=Количество-%s" 
            "WHERE Название=%s",(int(self.lineEdit_col.text()),self.lineEdit_mat.text(),))
            cursor.execute('INSERT INTO Расход(Номер_записи,Название,Количество) VALUES(%s,%s,%s)',(int(self.lineEdit_numb.text()),self.lineEdit_mat.text(),int(self.lineEdit_col.text()),))
            self.help.conn.commit()
            self.tableWidget.clearContents()
            self.fill_table_material()
            cursor.close()
            self.success.show()
        except:
            self.error.label_2.setText("Данные")
            self.show()