import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QListWidget,QListWidgetItem
)
class db():
    def __init__(self):
        self.conn = psycopg2.connect(dbname='салон красоты', user='annasarybaeva', host='localhost')
    def sql(self,req):
        cursor = self.conn.cursor()
        cursor.execute(req)
        return cursor
    def fill_table(self,cursor,tableWidget):
        tablerow=0
        for row in cursor:
            tableelem=0
            for elem in row:
                tableWidget.setItem(tablerow,tableelem,QtWidgets.QTableWidgetItem(str(elem)))
                tableelem+=1
            tablerow+=1
