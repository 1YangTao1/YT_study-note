import csv,requests
from bs4 import BeautifulSoup

with open('movie.csv','a',newline='',encoding='utf-8') as f:
    write = csv.writer(f)
    write.writerow(['电影名','评分','评语','链接'])
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(i*25) + '&filter='
        res = requests.get(url)
        html = res.text
        mov_list_soup = BeautifulSoup(html,'html.parser')
        mov_listss = mov_list_soup.find(class_='grid_view')
        mov_lists = mov_listss.find_all('li')
        for mov_list in mov_lists:
            mov_num = mov_list.find(class_='pic')
            mov_name = mov_list.find('span',class_='title')
            mov_url = mov_list.find('a')
            mov_score = mov_list.find(class_='rating_num')
            mov_comment = mov_list.find(class_='quote')
            name = mov_name.text
            urls = mov_url['href']
            score = mov_score.text
            try:
                comment=mov_comment.text
            except(AttributeError):
                comment = '无'
            write.writerow([name,score,comment,urls])
