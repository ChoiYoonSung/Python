import pymysql

def insertChicken(tuts):
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    
    curs = conn.cursor()
    sql = "insert into hello (col01, col02, col03) values(%s, %s, %s)"
    curs.executemany(sql, tuts)
    cnt = conn.commit()
    
    print(curs.rowcount, "record inserted") 
     
    conn.close()
    return cnt

if __name__ == '__main__':
    
    tuts = []
    tuts.append((1,'1','1'))
    tuts.append((2,'2','2'))
    tuts.append((3,'3','3'))
    insertChicken(tuts)