import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
html = res.text

soup = BeautifulSoup(html,'html.parser')

items = soup.find_all(class_='recentcomments')
for item in items:
    comment = item.find()

