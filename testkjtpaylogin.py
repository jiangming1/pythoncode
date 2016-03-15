# coding: UTF-8
#作者 蒋明
#作用 测试kjt登录脚本
#日期 2016-03-09
from selenium import webdriver
import time
runtag='fj052_mag_prod_build_20160308.1'
a='2016-3-9 02:00:00'
a_struck_time=time.strptime(a,'%Y-%m-%d %H:%M:%S')
print time.mktime(a_struck_time)
print time.time()
runtime=time.mktime(a_struck_time)
while runtime>time.time():
    time.sleep(6)
    print "wait"

driver=webdriver.Ie('d:/IEDriverServer.exe')
driver.get("https://www.kjtpay.com/login/page.htm")
driver.find_element_by_id("username").send_keys("13858101782@qq.com")
driver.find_element_by_id("checkbox_safepw").click()
driver.find_element_by_class_name("password").send_keys("jmdjsj903291A")
driver.find_element_by_id("kjt_personal_login_login").click()
time.sleep(5)
#driver.quit()