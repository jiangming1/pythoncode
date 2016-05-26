# coding: UTF-8
#作者 蒋明
#作用 cdn登录刷新缓存
#日期 2016-03-09
from selenium import webdriver
import time
import os

#from pyvirtualdisplay import Display
#import paramiko
import sys
reload( sys )
sys.setdefaultencoding('utf-8')

#display = Display(visible=0, size=(1280, 768))
#display.start()
runtag='fj052_mag_prod_build_20160308.1'
a='2016-3-9 02:00:00'
a_struck_time=time.strptime(a,'%Y-%m-%d %H:%M:%S')
print time.mktime(a_struck_time)
print time.time()
runtime=time.mktime(a_struck_time)
driver=webdriver.Firefox()
driver.set_window_size(1080,800)
driver.implicitly_wait(30)
driver.get("https://i.umeng.com/?ufrom=mobile.umeng.com%2F&app_id=umeng&redirectURL=http://mobile.umeng.com/apps")
driver.find_element_by_xpath("//*[@id=\"ump\"]/div[1]/div/form/div[1]/ul/li[1]/div/label/input").send_keys("wubo@laicunba.com")
driver.find_element_by_xpath("//*[@id=\"ump\"]/div[1]/div/form/div[1]/ul/li[2]/label/input").send_keys("138w709b")
driver.find_element_by_xpath("//*[@id=\"submitForm\"]").click()
time.sleep(1)
driver.get("http://mobile.umeng.com/apps/75c10090bfa55f0e72146d65/error_types/trend")
print driver.find_element_by_xpath("/html/body").text
#time.sleep(1)
#b=e.get_attribute("href")
#print b
#driver.find_element_by_xpath("//*[@id=\"export-top\"]").click()
#time.sleep(1)
#driver.get("http://mobile.umeng.com/apps/download_center")
#a=driver.find_element_by_xpath("//*[@id=\"file_5746a953e0f55acba300128f\"]/a")
#b=a.get_attribute("href")
#print b
    

