import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QPushButton, QRect
from PyQt5.QtCore import QSize
from _ast import If

form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.index = 0
        self.flag_bw = True
        self.black_cnt = 0
        self.white_cnt = 0
        self.setupUi(self)
        self.arr2d = [
                  [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
                , [0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
            ]
        
        self.pb2d = []
        for i in range(19):
            pb_line = []
            for j in range(19):
                tmp = QPushButton(self)
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(QRect(j*40+20,i*40+20,40,40))
                tmp.setToolTip(str(i) + "," + str(j))
                tmp.clicked.connect(self.BtnClick)
                pb_line.append(tmp)
            self.pb2d.append(pb_line)
        self.myrender()
        
    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QIcon('0.png'))
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QIcon('1.png'))
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QIcon('2.png'))
    
    def BtnClick(self):
        arr = (self.sender().toolTip()).split(",")
        i = int(arr[0])
        j = int(arr[1])
        if self.arr2d[i][j] > 0:
            return
        
        if self.flag_bw == True: #??????
            self.arr2d[i][j] = 1
            self.black_cnt += 1
            print("?????? : " + str(self.black_cnt) + "?????? ???")
        else: #??????
            self.arr2d[i][j] = 2
            self.white_cnt += 1
            print("?????? : " + str(self.white_cnt) + "?????? ???")
        
        self.myrender()
        self.flag_bw = not self.flag_bw
            
if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   sys.exit(app.exec_())