import requests,openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '张佳玮'
sheet['A1'] = 'title'
sheet['B1'] = 'url'
sheet['C1'] = 'excerpt'

header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3865.120 Safari/537.36'}
offset = 10
for i in range(3):
    url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?include=data%5B*%5D.comment_count%2Csuggest_edit%2Cis_normal%2Cthumbnail_extra_info%2Cthumbnail%2Ccan_comment%2Ccomment_permission%2Cadmin_closed_comment%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%2Cis_labeled%2Clabel_info%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&'+'offset='+str((i+1)*10)+'&limit=10&sort_by=created'
    res = requests.get(url,headers=header)
    json_text = res.json()
    for i in json_text['data']:
        sheet.append([i['title'],i['url'],i['excerpt']])
wb.save('张佳玮.xlsx')
    


