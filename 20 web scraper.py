import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.ml/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class':'post-title'})
print(title)

title[0].getText()
title1 = title[0].getText()
print(title1)

for t in title:
    print(t.getText())