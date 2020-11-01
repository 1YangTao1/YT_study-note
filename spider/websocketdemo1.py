import asyncio
import logging
import csv
from aiowebsocket.converses import AioWebSocket

'''
    1.这段程序每隔20+多个数据会暂停，报错
    2.这段程序是怎么运行的？
    3.实时的把数据存储在文件中
    4.
        sh600536=中国软件,72.080,72.010,71.810,73.310,71.600,71.800,71.810,10000727,725520253.000,8679,71.800,2800,71.790,1201,71.780,1300,71.770,2400,71.760,5600,71.810,12700,71.820,100,71.830,700,71.840,1400,71.850,2020-04-15,15:00:00,00,
        这种类型的数据进行处理     split   匹配 python字符串处理函数
    优化
    5.实时数据-> MongDB -> Mysql
    6. 每天开盘时间9点半到11点半，下午是1点到3点
    7.搞清楚每个字段的含义
'''
# Mongdb

async def startup(url):
    async with AioWebSocket(url) as aws:
        converse = aws.manipulator
        # 客户端给服务端发送消息,这个wsid参数是自己通过分析抓包获取到的心跳参数
        await converse.send('{"wsid":1}')
        num=0
        while True:
            mes = await converse.receive()
            # #这里是采用累计5的倍数时候，向服务器发送一次心跳，保持连接
            num+=1
            if num%5==0:
                await converse.send('{"wsid":1}')
            content= mes.decode('utf-8')
            Data=content.split(',')
            print(Data)
            with open('600694.csv','a+',encoding='UTF-8',newline='') as file:
                fieldnames={"Name"}
                w=csv.DictWriter(file,fieldnames=fieldnames)
                w=csv.writer(file)
                w.writerow(Data)
                #print("over")


if __name__ == '__main__':
    remote = 'wss://hq.sinajs.cn/wskt?list=sh600694'
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')