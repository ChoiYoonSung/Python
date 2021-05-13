import pymysql
import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def getPrices(s_name):
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
     
    sql = "select s_price   from stock where s_name = '{}' order by crawl_date".format(s_name)
    curs.execute(sql)
     
    rows = curs.fetchall()
    stock = []
    for row in rows:
        stock.append(row[0])
    conn.close()
    return np.array(stock)

def getNames():
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
     
    curs = conn.cursor()
     
    sql = "select s_name from stock group by s_name order by crawl_date"
    curs.execute(sql)
     
    rows = curs.fetchall()
    name = []
    for row in rows:
        name.append(row[0])
    conn.close()
    return np.array(name)

arr_name = getNames()

arr_z = []
for i in range(len(arr_name)):
    arr_z.append(getPrices(i))

arr_per_z = []
for i in range(len(arr_name)):
    temp = (arr_z[i]/arr_z[0][0])*100
    arr_per_z.append(temp)

z = np.array(getPrices('삼성전자'))
z1 = np.array(getPrices('삼성전자우'))
x = np.array([1,1,1,1,1,1,1,1,1,1])
y = np.array([0,1,2,3,4,5,6,7,8,9])

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x, y, arr_per_z[0], 'red')
ax.plot3D(x+1, y, arr_per_z[1], 'blue')
ax.set_title('3D line plot')
plt.show()