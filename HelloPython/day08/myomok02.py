import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QPushButton, QRect
from PyQt5.QtCore import QSize
from _ast import If

form_class = uic.loadUiType("myomok02.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.index = 0
        self.flag_bw = True
        self.flag_result = True
        self.black_cnt = 0
        self.white_cnt = 0
        self.setupUi(self)
        self.arr2d = [[0 for i in range(19)] for j in range(19)]
        
        self.pb2d = []
        for i in range(10):
            pb_line = []
            for j in range(10):
                tmp = QPushButton(self)
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(QRect(j*40+20,i*40+20,40,40))
                tmp.setToolTip(str(i) + "," + str(j))
                tmp.clicked.connect(self.BtnClick)
                pb_line.append(tmp)
            self.pb2d.append(pb_line)
        self.myrender()
        self.pbReset.clicked.connect(self.BtnReset)
    
    def BtnReset(self):
        self.index = 0
        self.flag_bw = True
        self.flag_result = True
        self.black_cnt = 0
        self.white_cnt = 0
        self.arr2d = [[0 for i in range(10)] for j in range(10)]
        self.myrender()
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QIcon('0.png'))
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QIcon('1.png'))
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QIcon('2.png'))
    
    def BtnClick(self):
        if not self.flag_result:
            return
        
        arr = (self.sender().toolTip()).split(",")
        i = int(arr[0])
        j = int(arr[1])
        if self.arr2d[i][j] > 0:
            return
        
        stone = 0;
        if self.flag_bw == True: #흑돌
            self.arr2d[i][j] = 1
            self.black_cnt += 1
            stone = 1
            print("흑돌 : " + str(self.black_cnt) + "번째 수")
        else: #백돌
            self.arr2d[i][j] = 2
            self.white_cnt += 1
            stone = 2
            print("백돌 : " + str(self.white_cnt) + "번째 수")
        
        up = self.getUp(i, j,stone)
        dw = self.getDw(i, j, stone)
        le = self.getLe(i, j, stone)
        ri = self.getRi(i, j, stone)
        ur = self.getUr(i, j,stone)
        dl = self.getDl(i, j, stone)
        ul = self.getUl(i, j, stone)
        dr = self.getDr(i, j, stone)
        
        d1 = up+dw+1
        d2 = le+ri+1 
        d3 = ur+dl+1
        d4 = ul+dr+1
        
        self.myrender()
        if 5 in (d1 , d2, d3, d4):
            winner = ""
            if self.flag_bw:
                winner = "흑"
            else:
                winner = "백"
            QtWidgets.QMessageBox.about(self, "GameSet", winner+"돌이 이겼습니다.")
            self.flag_result = False
        self.flag_bw = not self.flag_bw
        
    def getUp(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getDw(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getLe(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getRi(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getUr(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += -1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getDl(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getUl(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += -1
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getDr(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   sys.exit(app.exec_())