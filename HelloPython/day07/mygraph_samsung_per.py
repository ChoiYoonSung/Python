import pymysql
import numpy as np
import matplotlib.pyplot as plt
from random import random

conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()
def getPrices(s_name, i):
    sql = "select s_price from stock where s_name = '{}' order by crawl_date".format(s_name)
    curs.execute(sql)
     
    rows = curs.fetchall()
    stock = []
    for row in rows:
        stock.append((row[0]/rows[0][0])*100)
    
    stock_n = np.array(stock)
    return stock_n

def getName():
    sql = "select s_name from stock group by s_name order by crawl_date"
    curs.execute(sql)
     
    rows = curs.fetchall()
    name = []
    
    for row in rows:
        name.append(row[0])
    
    name_n = np.array(name)
    return name_n

def getNumpy(cnt, price):
    z = np.array(price)
    x = np.array([cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt])
    y = np.array([0,1,2,3,4,5,6,7,8,9])
    
    ax.plot3D(x, y, z, c=rndColor())
    ax.set_title('Stock Chart')

def rndColor():
    r = random()
    g = random()
    b = random()
    color = (r,g,b,1)
    return color

if __name__ == '__main__':
    getName = getName()
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    percent = ""
    temp = ""
    print("Stock Chart loading..")
    for i, name in enumerate(getName):
        getNumpy(i, getPrices(name, i))
        i += 1
        percent = str((i/ len(getName))*100)[:str((i/ len(getName))*100).index('.')]
        if not percent == temp:
             print(percent + "%")
             temp = percent
    
    conn.close()
    plt.show()