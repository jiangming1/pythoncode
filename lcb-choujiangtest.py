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
driver.get("http://test.laicunba.com/h5/login.htm?tab=account&=returnUrl=http://test.laicunba.com/h5/activity/lucky_draw.htm")

driver.find_element_by_id("mobileInput").send_keys("15158813009")
driver.find_element_by_id("loginPwdInput").send_keys("123456")
driver.find_element_by_id("btnLogin").click()

time.sleep(10)
while runtime<time.time():
    driver.get("http://test.laicunba.com/h5/activity/lucky_draw.htm")
    driver.find_element_by_class_name("btn_run").click()
    



