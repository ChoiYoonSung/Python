import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random

form_class = uic.loadUiType("myqt08.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.clickPb)
        
    def clickPb(self):
        dan = int(self.leDan.text())
        result = ""
        for i in range(1,10):
            ans = str(dan*i)
            print(ans)
            result += (str(dan) + " * " + str(i) + " = " + str(ans) + "\n")
            
        self.teResult.setText(result)
if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   sys.exit(app.exec_())