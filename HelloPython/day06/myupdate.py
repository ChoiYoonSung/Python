import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = """
        update hello 
        set col02 = %s, col03 = %s 
        where col01 = %s
    """
val = ('4', '4', 3)
cnt = curs.execute(sql, val)
print(cnt)

conn.commit()
print(curs.rowcount, "record updated") 
 
conn.close()