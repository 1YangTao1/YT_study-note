import requests

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

data = {
    'log':'spiderman',
    'pwd':'crawler334566',
    'wp-submit':'登录',
    'redirect_to':'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie' :'1',
}

login_in = requests.post(url,headers=headers,data=data)
cookies = login_in.cookies 
#调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies
url1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data1 = {
'comment': input('请输入你想要发表的评论：'),
'submit': '发表评论',
'comment_post_ID': '13',
'comment_parent': '0'
}
res = requests.post(url1,headers=headers,data=data1,cookies=cookies)
print(res.status_code)