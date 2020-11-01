from selenium import webdriver
import time

drive = webdriver.Chrome()
drive.get('https://xinyue.qq.com/act/a20200428dnfbackflow/index_pc.html?ADTAG=AD_gw.gamezone.banner.1_DNF.20200525')

time.sleep(5)
print(drive.find_elements_by_xpath('//*[@id="qlogin_list"]/a[1]'))
#button1 = drive.find_elements_by_id('img_out_2495745362').get_attribute('src')
#print(button1)
#drive.get(button1)
#time.sleep(5)
#button1.find_element_by_css_selector('#qlogin_list a').click()
#print(button1.text)
time.sleep(3)
button2 = drive.find_element_by_xpath('//*[@id="lotterycontent_start"]')
button2.click()
button3 = drive.find_elements_by_xpath('/html/body/div[4]/div[4]/div[2]/div/a[2]')
button3.click()

time.sleep(3)
