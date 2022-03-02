from PyQt5 import QtCore, QtGui, QtWidgets

class MasterWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.build()
        
    def build(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('NoTittle')   