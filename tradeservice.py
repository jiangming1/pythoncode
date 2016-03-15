# coding: UTF-8
#作者 蒋明
#作用 定点执行指定的web脚本 模拟人的操作去执行一系列动作
#日期 2016-03-09
from selenium import webdriver
import time
runtag='fj058_tradeservice_prod_build_20160315.1'
a='2016-3-16 02:00:00'
a_struck_time=time.strptime(a,'%Y-%m-%d %H:%M:%S')
print time.mktime(a_struck_time)
print time.time()
runtime=time.mktime(a_struck_time)
while runtime>time.time():
    time.sleep(6)
    print "wait"
driver=webdriver.Firefox()
driver.get("http://192.168.180.18:8080/login?from=/")
driver.find_element_by_id("j_username").clear()
driver.find_element_by_id("j_username").send_keys("jiangming")
driver.find_element_by_name("j_password").send_keys("kjt@123")
driver.find_element_by_id("yui-gen1-button").click()
time.sleep(3)
driver.get("http://192.168.180.18:8080/view/%E7%94%9F%E4%BA%A7%E7%8E%AF%E5%A2%83/job/fj058_tradeservice_prod_deploy/build?delay=0sec")
driver.find_element_by_class_name("setting-input").send_keys(runtag)
#driver.find_element_by_id("yui-gen1-button").click()
time.sleep(3)
driver.get("http://192.168.180.18:8080/view/%E7%81%BE%E5%A4%87%E7%8E%AF%E5%A2%83/job/fj058_tradeservice_prod_deploy/build?delay=0sec")
driver.find_element_by_class_name("setting-input").send_keys(runtag)
driver.find_element_by_id("yui-gen1-button").click()
time.sleep(3)
#yui-gen1-button
print driver.title
time.sleep(5)
driver.quit()