from admin_win.dialog_win.error import Ui_Dialog
from admin_win.dialog_win.good import Ui_Dialog_good
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
class error(QMainWindow,Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class good(QMainWindow,Ui_Dialog_good):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
