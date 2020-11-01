import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%')

text = res.text

with open ('HTTP.txt','a+',encoding='utf-8') as f1:
    f1.write(text)
    f1.close()