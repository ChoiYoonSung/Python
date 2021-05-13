import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

form_class = uic.loadUiType("myqt01.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.index = 0
        self.setupUi(self)
        self.pb.clicked.connect(self.clickPb)
        
    def clickPb(self):
        self.index += 1
        loc_index = self.index % 3
        self.pb.setIcon(QIcon(str(loc_index) + '.png'))
        print(self.pb)
if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   sys.exit(app.exec_())