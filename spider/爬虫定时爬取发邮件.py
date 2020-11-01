import requests
from bs4 import BeautifulSoup
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import schedule,time

def spider_mseeage():
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    url = 'http://www.weather.com.cn/weather/101110101.shtml'
    res = requests.get(url,headers=headers)
    res.encoding = 'uft-8'
    #不确定编码方式时，可查看网页源代码，搜索charset即可
    weathersoup = BeautifulSoup(res.text,'html.parser')
    weather = weathersoup.find(class_='t clearfix')
    weat = weather.find('li')
    wea = weat.find('p',class_='wea')
    tem = weat.find(class_='tem').find('i')
    wea = wea.text
    tem = tem.text
    return wea,tem


from_addr = input('输入发送邮箱：')
to_addr = input('输入收件邮箱：')

def send_email(wea,tem):
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)

    password = 'krzwqhzurpziecja'
    qqmail.login(from_addr,password)

    content = '亲爱的,今天的天气是' + tem + wea
    message = MIMEText(content,'plain','utf-8')
    #实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码.
    subject = '今日天气预报'
    message['Subject'] = Header(subject,'utf-8')
    message['From'] = Header(from_addr)
    message['To'] = Header(to_addr)
    try:
        qqmail.sendmail(from_addr,to_addr,message.as_string())
        print('ok')
    except:
        print('no')
    qqmail.quit()

def job():
    print('开始一次任务：')
    wea,tem = spider_mseeage()
    send_email(wea,tem)
    print('任务完成')

schedule.every().day.at('07:30').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
