import requests,re
from bs4 import BeautifulSoup
from urllib.request import quote


header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3865.120 Safari/537.36'}
search = input('please input search item (0 is quit)')
while search != '0':
    try:
        if search == '0':
            exit(0)
        url = 'https://baike.baidu.com/item/'+ str(quote(search))
        res = requests.get(url,headers=header,)
        res.encoding='utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        contents = soup.find('div',class_='lemma-summary').find_all('div',class_='para')
        for i in contents:
            item = re.sub(re.compile('\s'),'',i.text)
            items = re.sub(re.compile('\[(.+?)\]'),'',item)
            print(items,'\n')
    except:
        print('sorry not have anything')
    search = input('please input search item (0 is quit)')
    
    



    
