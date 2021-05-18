import pymysql

class DaoExam:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
        
    def myselect(self):
        ret = []
        curs = self.conn.cursor()
 
        sql = "select e_id, kor, eng, math from exam"
        curs.execute(sql)
         
        rows = curs.fetchall()
        for row in rows:
            ret.append({'e_id' : row[0], 'kor' : row[1], 'eng' : row[2], 'math' : row[3]})
        return ret
    
    def myinsert(self, e_id, kor, eng, math):
        curs = self.conn.cursor()
        sql = f"insert into exam (e_id, kor, eng, math) values('{e_id}',{kor},{eng},{math})"
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def myupdate(self, e_id, kor, eng, math):
        curs = self.conn.cursor()
        sql = f"update exam set kor = {kor}, eng = {eng}, math = {math} where e_id = {e_id}"
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def mydelete(self, e_id):
        curs = self.conn.cursor()
        sql = f"delete from exam where e_id = '{e_id}'"
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.conn.close()
    
if __name__ == '__main__':
    de = DaoExam()
    # list = de.myselect()
    # cnt = de.myinsert('2','2','2')
    cnt = de.myupdate('2','4','4')
    # cnt = de.mydelete('2')
    # print(list)
    print(cnt)