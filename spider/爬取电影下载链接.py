import requests
from bs4 import BeautifulSoup
from urllib.request import quote

mov_name = input('输入你想要下载的电影名：')
name_gbk = mov_name.encode('gbk')
url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword=' + str(quote(name_gbk))
res1 = requests.get(url)
html = res1.text
mov_url = BeautifulSoup(html,'html.parser')
urls = mov_url.find(width="55%")
url2 = urls.find('a')
print('ygdy8.com'+url2['href'])


