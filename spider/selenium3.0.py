from selenium import webdriver
import time

drive = webdriver.Chrome()
drive.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)
user_login = drive.find_element_by_xpath('//*[@id="user_login"]')
user_login.send_keys('spiderman')
user_pass = drive.find_element_by_xpath('//*[@id="user_pass"]')
user_pass.send_keys('crawler334566')
button1 = drive.find_element_by_xpath('//*[@id="wp-submit"]')
button1.click()
time.sleep(2)
button2 = drive.find_element_by_xpath('//*[@id="post-20"]/header/h2/a')
button2.click()
time.sleep(2)
commet = drive.find_element_by_xpath('//*[@id="comment"]')
commet.send_keys('selenium is very good!s')
button3 = drive.find_element_by_xpath('//*[@id="submit"]')
button3.click()
time.sleep(3)
drive.close()

