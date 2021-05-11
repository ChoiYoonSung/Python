import requests
from bs4 import BeautifulSoup

url = 'http://localhost:90/CRAWL/crawl.html'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select_one('table.basic1')
    
    tds = table.select('tr > td')
    for i, td in enumerate(tds):
        if i > 1:
            print(td.get_text())
else : 
    print(response.status_code)