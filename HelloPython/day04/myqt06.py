import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random

form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.clickPb)
        
    def clickPb(self):
        num1 = int(self.le1.text())
        num2 = int(self.le2.text())
        numResult = 0
        
        arr = range(num1, num2+1)
        for i in arr:
            if i%2 == 0:
                numResult += i
            
        self.leResult.setText(str(numResult))

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   sys.exit(app.exec_())