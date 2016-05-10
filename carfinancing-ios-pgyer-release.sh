# coding: UTF-8
#作者 蒋明
#作用 定点模拟登陆购买融融车贷

#日期 2016-03-09

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
ß
runtag='fj050_site_prod_build_20160315.1'
a='2016-3-15 21:00:00'
a_struck_time=time.strptime(a,'%Y-%m-%d %H:%M:%S')
print time.mktime(a_struck_time)
print time.time()
runtime=time.mktime(a_struck_time)
while runtime>time.time():
    time.sleep(6)
    print "wait"
d=webdriver.Firefox()
d.get("http://8.hzrrcd.com/h5/login.htm?tab=account")
d.find_element_by_id("mobileInput").send_keys("13291488404x")
d.find_element_by_id("loginPwdInput").send_keys("opewoxqxxx")
d.find_element_by_id("loginPwdInput").send_keys(Keys.ENTER)
time.sleep(1)
d.get("http://8.laicunba.com/h5/bid_form.htm?id=5577659b-a96e-45ec-873e-f0fd4b75600d")
d.find_element_by_id("buyAmountInput").send_keys("1000")
d.find_element_by_id("btnSubmit").click()
time.sleep(1)
d.find_element_by_id("getYzm").click()
d.find_element_by_name("yzm").send_keys("0000")
d.find_element_by_name("paybtn").click()
time.sleep(20)
d.quit()
