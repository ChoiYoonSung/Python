import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import random

form_class = uic.loadUiType("myqt09.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.clickPb1)
        self.pb2.clicked.connect(self.clickPb2)
        self.pb3.clicked.connect(self.clickPb3)
        self.pb4.clicked.connect(self.clickPb4)
        self.pb5.clicked.connect(self.clickPb5)
        self.pb6.clicked.connect(self.clickPb6)
        self.pb7.clicked.connect(self.clickPb7)
        self.pb8.clicked.connect(self.clickPb8)
        self.pb9.clicked.connect(self.clickPb9)
        self.pb0.clicked.connect(self.clickPb0)
        self.pbCall.clicked.connect(self.clickPbCall)
        
    def clickPb1(self):
        txt = self.pb1.text()
        le = self.le.text() + txt
        self.le.setText(le)
        
    def clickPb2(self):
        txt = self.pb2.text()
        le = self.le.text() + txt
        self.le.setText(le)
        
    def clickPb3(self):
        txt = self.pb3.text()
        le = self.le.text() + txt
        self.le.setText(le)
        
    def clickPb4(self):
        txt = self.pb4.text()
        le = self.le.text() + txt
        self.le.setText(le)
        
    def clickPb5(self):
        txt = self.pb5.text()
        le = self.le.text() + txt
        self.le.setText(le)
        
    def clickPb6(self):
        txt = self.pb6.text()
        le = self.le.text() + txt
        self.le.setText(le)
        
    def clickPb7(self):
        txt = self.pb7.text()
        le = self.le.text() + txt
        self.le.setText(le)
        
    def clickPb8(self):
        txt = self.pb8.text()
        le = self.le.text() + txt
        self.le.setText(le)
        
    def clickPb9(self):
        txt = self.pb9.text()
        le = self.le.text() + txt
        self.le.setText(le)
        
    def clickPb0(self):
        txt = self.pb0.text()
        le = self.le.text() + txt
        self.le.setText(le)
    
    def clickPbCall(self):
        le = self.le.text()
        msg = QMessageBox()
        msg.setText("Calling to " + le + "..")
        msg.setWindowTitle("Call")
        msg.exec_()
         
if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   sys.exit(app.exec_())