import os
import sys
import urllib.request
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    soup = BeautifulSoup(response_body, 'html.parser')
    stockInfos = soup.select('td.st2')
    
    for i, stockInfo in enumerate(stockInfos):
        s_code = stockInfo.select_one('a').attrs['title']
        s_name = stockInfo.text
        s_price = stockInfo.find_next_sibling("td").text.replace(",","")
        
else:
    print("Error Code:" + rescode)