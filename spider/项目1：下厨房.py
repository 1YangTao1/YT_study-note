import requests
from bs4 import BeautifulSoup

menus = []
res = requests.get('http://www.xiachufang.com/explore/')
html = res.text

soup = BeautifulSoup(html,'html.parser')

message = soup.find_all('div',class_='info pure-u')

for i in message:
    dish_name = i.find('a')
    food_material = i.find('p',class_='ing ellipsis')
    url = 'http://www.xiachufang.com'+dish_name['href']
    menu = []
    menu.append(dish_name.text[17:13])
    menu.append(url)
    menu.append(food_material.text[1:-1])
    menus.append(menu)
print(menus)


