import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random

form_class = uic.loadUiType("myqt05.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.clickPb)
        
    def clickPb(self):
        mine = self.leMine.text()
        com = ""
        result = ""
        rnd = random.random()
        
        if rnd <= 0.5:
            com = "홀"
        else:
            com = "짝"
        
        if mine== com :
            result = "이겼습니다."
        else:
            result = "졌습니다."
        
        self.leCom.setText(com)
        self.leResult.setText(result)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   sys.exit(app.exec_())