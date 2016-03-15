# coding: UTF-8
#作者 蒋明
#作用 cdn登录刷新缓存
#日期 2016-03-09
from selenium import webdriver
import time
import os

a='2016-3-15 21:10:00'
a_struck_time=time.strptime(a,'%Y-%m-%d %H:%M:%S')
print time.mktime(a_struck_time)
print time.time()
runtime=time.mktime(a_struck_time)
while runtime>time.time():
    time.sleep(6)
    print "wait"

driver=webdriver.Firefox()
driver.get("https://portal.chinanetcenter.com/cas/login?service=https%3A%2F%2Fsi.chinanetcenter.com%2Fr_sec_login")
driver.find_element_by_id("username").send_keys("yunwei2016")
out=False
while out==False:
    driver.find_element_by_id("jcaptchaImage").click()
    time.sleep(1)
    driver.get_screenshot_as_file('/google.png')
#自动效验验证码
    cmd ="cd /"
    print cmd
    os.system(cmd)
    cmd ="convert /google.png -crop 94x35+446+354 /google1.png"
    print cmd
    os.system(cmd)
    cmd ="tesseract /google1.png /result"
    print cmd
    os.system(cmd)
    f = open("/result.txt", "r")
    line = f.readline()
    f.close()
    if len(line)==5:
        out=True
time.sleep(5)

driver.find_element_by_id("password").send_keys("yunwei@2016")
driver.find_element_by_id("jcaptcha").send_keys(line)
driver.find_element_by_id("login-btn").click()
driver.get("https://si.chinanetcenter.com/purview/contentManage/update_directory.html?CODE=SI_CP_PURGE_DIRECTORY&productCode=SI_CONTENT_MANAGE")
driver.find_element_by_id("J_dir_text").send_keys("https://static.kjtpay.com/")
driver.get_screenshot_as_file('/googleend.png')

