from gevent import monkey
monkey.patch_all()
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步
#它能给程序打上补丁，让程序变成是异步模式，而不是同步模式。它也叫“猴子补丁”。
import gevent,requests,time
from gevent.queue import Queue
#从gevent库里导入Queue模块

start = time.time()

url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

work = Queue()
#创建队列对象，并赋值于work
for url in url_list:
    work.put_nowait(url)
    #将url放入队列里边

#创建访问网站的函数
def crawler():
    while not work.empty():
        url = work.get_nowait()
        #将网址从队列中取出来
        r = requests.get(url)
        print(url,work.qsize(),r.status_code)

task_list = []
#创建空的任务列表
for x in range(2):
#相当于创建了两个爬虫
    task = gevent.spawn(crawler)
    #用gevent.spawn()创建执行crawler()函数的任务
    task_list.append(task)
    #往任务列表添加任务
gevent.joinall(task_list)
#执行所有任务
end = time.time()
print(end-start)
