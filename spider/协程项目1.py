from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
import requests,gevent,csv
from bs4 import BeautifulSoup
que = Queue()
for i in range(1,12):
    if i!=11:
        url1 ='http://www.boohee.com/food/group/'+str(i)+'?page='
    else:
        url1 = 'http://www.boohee.com/food/view_menu?page='
    for j in range(1,4):
        url2 = url1 + str(j)
        que.put_nowait(url2)


def crawler():
    with open('shiwu.csv','w',newline='') as f:
        write = csv.writer(f)
        write.writerow(['食物','热量','链接'])
        headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        while not que.empty():
            url = que.get_nowait()
            res = requests.get(url,headers=headers)
            soup = BeautifulSoup(res.text,'html.parser')
            foods = soup.find_all('li', class_='item clearfix')
            for food in foods:
                food_name = food.find_all('a')[1]['title']
                food_url = 'http://www.boohee.com' + food.find_all('a')[1]['href']
                food_calorie = food.find('p').text
                write.writerow([food_name,food_calorie,food_url])

task_list = []
for i in range(5):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
            





    
    

