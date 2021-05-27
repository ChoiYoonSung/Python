import sys
import numpy as np
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QPushButton, QRect
from PyQt5.QtCore import QSize
from tensorflow.keras.models import load_model
model = load_model('models/20201213_202430.h5')
form_class = uic.loadUiType("myomok20.ui")[0]

def getCom(arr2d):
    input = np.zeros((20,20))
    for i in range(20):
        for j in range(20):
            if arr2d[i][j] == 2:
                input[i][j] = -1
            elif arr2d[i][j] == 1:
                input[i][j] = 1
    
    input = input.reshape(1,20,20,1)
    
    output = model.predict(input).squeeze()
    output = output.reshape((20, 20))
    for i in range(20):
        for j in range(20):
            if arr2d[i][j] > 0:
                output[i][j] = 0
    i, j = np.unravel_index(np.argmax(output), output.shape)
    return i,j
    
class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.black_cnt = 0
        self.white_cnt = 0
        self.stone = 0
        self.winner = ""
        self.flag_bw = True
        self.flag_result = True
        self.setupUi(self)
        self.arr2d = [[0 for i in range(20)] for j in range(20)]
        
        self.pb2d = []
        for i in range(20):
            pb_line = []
            for j in range(20):
                tmp = QPushButton(self)
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(QRect(j*40,i*40,40,40))
                tmp.setToolTip(str(i) + "," + str(j))
                tmp.clicked.connect(self.BtnClick)
                pb_line.append(tmp)
            self.pb2d.append(pb_line)
        self.myrender()
        self.pbReset.clicked.connect(self.BtnReset)
        self.lbl.setText("오목 준비중")
    
    
    def BtnReset(self):
        self.black_cnt = 0
        self.white_cnt = 0
        self.stone = 0
        self.winner = ""
        self.flag_bw = True
        self.flag_result = True
        self.arr2d = [[0 for i in range(20)] for j in range(20)]
        self.myrender()
        self.lbl.setText("오목 준비중")
        
        
    def myrender(self):
        for i in range(20):
            for j in range(20):
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
        
        self.arr2d[i][j] = 1
        self.black_cnt += 1
        self.stone = 1
        print("흑돌 : " + str(self.black_cnt) + "번째 수")
        self.lbl.setText("백돌 차례")
        
        self.win(i, j, self.stone)
        self.com()
    
    
    def com(self):
        if not self.flag_result:
            return
        
        i,j = getCom(self.arr2d)
        
        self.arr2d[i][j] = 2
        
        self.white_cnt += 1
        self.stone = 2
        print("백돌 : " + str(self.white_cnt) + "번째 수")
        self.lbl.setText("흑돌 차례")
        
        self.win(i, j, self.stone)
    
    
    def win(self,i,j,stone):
        up = self.getUp(i, j, stone)
        dw = self.getDw(i, j, stone)
        le = self.getLe(i, j, stone)
        ri = self.getRi(i, j, stone)
        ur = self.getUr(i, j, stone)
        dl = self.getDl(i, j, stone)
        ul = self.getUl(i, j, stone)
        dr = self.getDr(i, j, stone)
        
        d1 = up+dw+1
        d2 = le+ri+1 
        d3 = ur+dl+1
        d4 = ul+dr+1
        
        self.myrender()
        if 5 in (d1 , d2, d3, d4):
            if self.flag_bw:
                self.winner = "흑"
            else:
                self.winner = "백"
            QtWidgets.QMessageBox.about(self, "GameSet", self.winner+"돌이 이겼습니다.")
            self.lbl.setText("승자 : " + self.winner)
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