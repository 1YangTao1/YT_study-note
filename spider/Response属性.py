import requests
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
print(res.status_code)
#打印变量res的响应状态码，以检查是否请求成功
# 100收到请求  200请求成功 305应使用代理访问 403禁止访问 503服务器不可用
res.encoding = 'utf-8'
#定义Response对象的编码。
pic=res.content
#把Reponse对象的内容以二进制数据的形式返回
photo = open('ppt.jpg','wb')
#新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
#图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
photo.write(pic) 
photo.close()
#图片、音频、视频的下载


#引用requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
novel=res.text
#把Response对象的内容以字符串的形式返回
with open ('novel.txt','a',encoding='utf-8') as novels:
    novels.write(novel)
#文字、网页源代码的下载
    novels.close()