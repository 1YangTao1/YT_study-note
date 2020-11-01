import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/')
html = res.text

soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for item in items:
    comment = item.find('p')
    name = item.find('h3')
    price = item.find(class_='price_color')
    print(comment['class'][1])
    print(name.text)
    print(price.text)

'''kind = items.find_all('li')
for i in kind:
    print(i.text)'''