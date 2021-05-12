from datetime import datetime
import os
import sys
import urllib.request

from bs4 import BeautifulSoup
import pymysql
import time


def insertStock(tuts):
   conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
   
   curs = conn.cursor()
   sql = "insert into stock (s_code, s_name, s_price, crawl_date) values(%s, %s, %s, %s)"
   cnt = curs.executemany(sql, tuts)
   conn.commit()
   
   print(curs.rowcount, "record inserted") 
    
   conn.close()
   return cnt

for i in range(10):
    url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        
        soup = BeautifulSoup(response_body, 'html.parser')
        stockInfos = soup.select('td.st2')
        
        now = datetime.now()
        crawl_date = now.strftime('%m.%d %H:%M')
        
        tuts = []
        for i, stockInfo in enumerate(stockInfos):
            s_code = stockInfo.select_one('a').attrs['title']
            s_name = stockInfo.text
            s_price = stockInfo.find_next_sibling("td").text.replace(",","")
            tuts.append((s_code, s_name, s_price, crawl_date))
            
        cnt = insertStock(tuts)
        print("crawl time : " + str(crawl_date))
        print("cnt : " + str(cnt))
    else:
        print("Error Code:" + rescode)
        
    time.sleep(60)