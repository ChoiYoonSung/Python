import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

form_class = uic.loadUiType("myqt02.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.clickPb)
        
    def clickPb(self):
        txt = int(self.lbl.text())
        txt += 1
        self.lbl.setText(str(txt))

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   sys.exit(app.exec_())