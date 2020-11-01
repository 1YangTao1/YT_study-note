import requests,openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'restaurants'

sheet['A1'] = '歌曲名'
sheet['B1'] = '所属专辑'
sheet['C1'] = '播放时长'
sheet['D1'] = '播放连接'

headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }

for i in range(5):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61119291623654599&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=' +str(i+1)+'&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    res = requests.get(url,headers=headers)
    json_mus = res.json()
    for i in json_mus['data']['song']['list']:
        name = i['name']
        album = i['album']['name']
        time = str(int(i['interval']/60))+':'+str(i['interval']%60)
        link =  'https://y.qq.com/n/yqq/song/'+i['mid'] +'.html'
        sheet.append([name,album,time,link])
        #print(i['name'] + '  专辑：'+ i['album']['name'] + '   时长：' + str(int(i['interval']/60))+':'+str(i['interval']%60))
        #print('链接：https://y.qq.com/n/yqq/song/'+i['mid'] +'.html\n')
wb.save('Jay.xlsx')