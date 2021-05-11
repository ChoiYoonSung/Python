import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
tuts = (
    (1,'1','1')
    , (2,'2','2')
    , (3,'3','3')
    )
sql = "insert into hello (col01, col02, col03) values(%s, %s, %s)"
curs.executemany(sql, tuts)
conn.commit()

print(curs.rowcount, "record inserted") 
 
conn.close()