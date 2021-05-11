import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = "delete from hello where col01 = %s"
val = (3)
curs.execute(sql, val)

conn.commit()
print(curs.rowcount, "record deleted") 
 
conn.close()