import requests,json
session = requests.session()
#用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies。

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

data = {
    'log':'spiderman',
    'pwd':'crawler334566',
    'wp-submit':'登录',
    'redirect_to':'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie' :'1',
}
session.post(url,headers = headers,data=data)
cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
#把cookies转化成字典。

cookies_str = json.dumps(cookies_dict)
#调用json模块的dumps函数，把cookies从字典再转成字符串loads与之相反。dump函数和load函数用来处理文件中的数据
with open ('cookies.txt','w') as f:
    f.write(cookies_str)

url1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data1 = {
'comment': input('请输入你想要发表的评论：'),
'submit': '发表评论',
'comment_post_ID': '13',
'comment_parent': '0'
}

session.post(url1,headers = headers,data=data1)
#在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数

