from bs4 import BeautifulSoup
from email.header import Header
from email.mime.text import MIMEText
import smtplib,schedule,time,requests


def menus():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')

    list_all = []

    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        list_all.append([name,URL,ingredients])
    return list_all

def send_mail(menu):
    from_addr = '2495745362@qq.com'
    password = 'krzwqhzurpziecja'
    content = ''
    for i in menu:
        content +=str(i)
    to_addr = '2495745362@qq.com'

    mail_host = 'smtp.qq.com'
    qqemail = smtplib.SMTP()
    qqemail.connect(mail_host,25)
    qqemail.login(from_addr,password)

    mseeage = MIMEText(content,'plain','utf-8')
    subject = '本周最佳菜单'
    mseeage['Subject'] = Header(subject)
    mseeage['From'] = Header(from_addr)
    mseeage['To'] = Header(to_addr)

    try:
        qqemail.sendmail(from_addr,to_addr,mseeage.as_string())
        print('发送成功')
    except:
        print('发送失败')
    qqemail.quit()

def job():
    print('第一次开始任务')
    menu = menus()
    send_mail(menu)
    print('任务完成')

schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)




