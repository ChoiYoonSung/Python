import pymysql
import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def getPrices(s_name):
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
     
    curs = conn.cursor()
     
    sql = "select s_price   from stock where s_name = '{}' order by crawl_date".format(s_name)
    curs.execute(sql)
     
    rows = curs.fetchall()
    stock = []
    for row in rows:
        stock.append(row[0])
    
    stock_n = np.array(stock)
    conn.close()
    return stock_n

fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.array(getPrices('삼성전자'))
z1 = np.array(getPrices('삼성전자우'))
x = np.array([1,1,1,1,1,1,1,1,1,1])
y = np.array([0,1,2,3,4,5,6,7,8,9])

print(z)

ax.plot3D(x, y, z, 'red')
ax.plot3D(x+1, y+1, z1, 'blue')
ax.set_title('3D line plot')
plt.show()