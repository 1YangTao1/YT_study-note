import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#向服务器发送一个请求，括号你是你需要数据的网址，对服务请求做出了响应
#把响应的结果值赋给res
print(res.status_code)
#打印变量res的响应状态码，以检查是否请求成功
# 100收到请求  200请求成功 305应使用代理访问 403禁止访问 503服务器不可用