import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random

form_class = uic.loadUiType("myqt07.ui")[0]

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

        if rnd <= 0.3:
            com = "가위"
        elif rnd > 0.3 and rnd <= 0.6:
            com = "바위"
        else:
            com = "보"
        
        if mine == "가위" and com == "가위":
            result = "비겼습니다."
        elif mine == "가위" and com == "바위":
            result = "졌습니다."
        elif mine == "가위" and com == "보":
            result = "이겼습니다."
            
        elif mine == "바위" and com == "가위":
            result = "이겼습니다."
        elif mine == "바위" and com == "바위":
            result = "비겼습니다."
        elif mine == "바위" and com == "보":
            result = "졌습니다."
            
        elif mine == "보" and com == "가위":
            result = "졌습니다."
        elif mine == "보" and com == "바위":
            result = "이겼습니다."
        elif mine == "보" and com == "보":
            result = "비겼습니다."
        
        self.leCom.setText(com)
        self.leResult.setText(result)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   sys.exit(app.exec_())