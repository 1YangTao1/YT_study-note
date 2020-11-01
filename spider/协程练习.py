import requests,gevent
from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
from bs4 import BeautifulSoup

#first 将所有url存入列表
url_list = []
for i in range(10):
    if i == 0:
        url = 'http://www.mtime.com/top/tv/top100/'
    else:

        url = 'http://www.mtime.com/top/tv/top100/index-'+ str(i+1) + '.html'
    url_list.append(url)

#second 创建队列将url入队
que = Queue()
for url in url_list:
    que.put_nowait(url)

#third 创建爬虫函数
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
def crawler():
    while not que.empty():
        url = que.get_nowait()
        res = requests.get(url,headers=headers)
        html = res.text
        soup = BeautifulSoup(html,'html.parser')
        teleplays = soup.find(id = 'asyncRatingRegion').find_all('li')
        for i in teleplays:
            tele = i.find(class_='mov_con')
            tele_name = tele.find('h2')
            tele_personnel = tele.find_all('p')
            tele_director = tele_personnel[0].find('a')
            try:
                tele_actors = tele_personnel[1].find_all('a')
            except:
                tele_actors = ''
            tele_comment = tele.find(class_='mt3')
            print('名字：' + tele_name.text)
            
            
            try:
                print(tele_director.text)
                for i in tele_actors:
                    print(i.text)
                print(tele_comment.text)
            except:
                print('NULL')

#forth 创建任务列表,编写执行任务程序
task_list = []
task = gevent.spawn(crawler)
task_list.append(task)
gevent.joinall(task_list)






