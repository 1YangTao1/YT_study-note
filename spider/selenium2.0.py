from selenium import webdriver
import time

drive = webdriver.Chrome()
drive.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
time.sleep(3)
button = drive.find_element_by_xpath('//*[@id="comment_box"]/div[3]/div/div[2]/a')
button.click()
comment = drive.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')
for i in comment:
    sweet = i.find_element_by_tag_name('p')
    print(sweet.text)
time.sleep(3)
drive.close()
#pagesourse = drive.page_source 获取网页html内容  随后可用bs4解析
#https://seleniumhq.github.io/selenium/docs/api/py/api.html 官方文档(英文)
#https://seleniumhq.github.io/selenium/docs/api/py/api.html 参考(中文)
