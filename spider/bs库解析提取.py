import requests
from bs4 import BeautifulSoup

res = requests.get(' https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

html = res.text

'''with open ('a.txt','a+',encoding='utf-8') as f1:
    f1.write(novel)
    f1.close()'''
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='books')
for item in items:
    kind = item.find('h2')
    title = item.find(class_='title')
    brief = item.find(class_='info')
    print(kind.text)
    print(title['href'])
    print(brief.text)
    print(type(kind),type(title),type(brief))


