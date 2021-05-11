import os
import sys
import urllib.request
from bs4 import BeautifulSoup

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
    soup = BeautifulSoup(response_body, 'html.parser')
    channel = soup.select_one('channel')
    titles = channel.select('channel > item > title')
    descriptions = channel.select('channel > item > description')
    a = 0
    for title, description in zip(titles, descriptions):
        stringTitle = title.get_text()
        stringDesc = description.get_text()
        characters = "</b>"
        for i in range(len(characters)):
            stringTitle = stringTitle.replace(characters[i], "")
            stringDesc = stringDesc.replace(characters[i], "")
        a += 1
        print(str(a) + "번 Title : " + stringTitle)
        print("   Content : " + stringDesc)
        print()
    
else:
    print("Error Code:" + rescode)