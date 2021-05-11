import os
import sys
import pymysql
import urllib.request
from bs4 import BeautifulSoup
from conda.core import link
 
def insertChicken(tuts):
   conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
   
   curs = conn.cursor()
   sql = "insert into chicken (title, link, description, bloggername, bloggerlink, postdate) values(%s, %s, %s, %s, %s, %s)"
   cnt = curs.executemany(sql, tuts)
   conn.commit()
   
   print(curs.rowcount, "record inserted") 
    
   conn.close()
   return cnt
 
client_id = "1XMSbNHcm41XMKSNtw5J"
client_secret = "9PQbU69VlL"
encText = urllib.parse.quote("치킨")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read().decode("UTF-8")
    soup = BeautifulSoup(response_body, 'xml')
    
    items = soup.select('item')
    tuts = []
    for i, item in enumerate(items):
        title = item.title.text
        link = item.link.text
        description = item.description.text
        bloggername = item.bloggername.text
        bloggerlink = item.bloggerlink.text
        postdate = item.postdate.text
        tuts.append((title, link, description, bloggername, bloggerlink, postdate))
        
    cnt = insertChicken(tuts)
    print("cnt",cnt)
        
else:
    print("Error Code:" + rescode)