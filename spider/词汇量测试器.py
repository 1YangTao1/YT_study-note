import requests,json

def request(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3865.120 Safari/537.36'}
    res = requests.get(url,headers=headers)
    json_text = res.json()
    return json_text


j=0
url1 = 'https://www.shanbay.com/api/v1/vocabtest/category/?_=1572527840452'
json_text1 = request(url1)
for i in json_text1['data']:
    print(j,end='.')
    print(i[1])
    j+=1
select = int(input('选择出题范围(0-9)：'))
if select == 0:
    url2 ='https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=GMAT&_=1572661786539'
elif select == 1:
    url2 ='https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=NGEE&_=1572661834056' 
elif select == 2:
    url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=NCEE&_=1572661873903'
elif select == 3:
    url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=CET4&_=1572661946115'
elif select == 4:
    url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=CET6&_=1572661988518'
elif select ==5:
    url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=TEM&_=1572662104653'
elif select == 6:
    url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=TOEFL&_=1572662137120'
elif select == 7:
    url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=GRE&_=1572662171808'
elif select == 8:
    url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=IELTS&_=1572662205819'
else :
    url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=NONE&_=1572662248857'
json_text2 = request(url2)


