# coding: UTF-8
#作者 蒋明
#作用 cdn登录刷新缓存
#日期 2016-03-09
from selenium import webdriver
import time
import os

from pyvirtualdisplay import Display
import paramiko
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
while runtime>time.time():
    time.sleep(6)
    print "wait"
driver=webdriver.Ie("d:/IEDriverServer.exe")
driver.implicitly_wait(30)
driver.get("https://www.kjtpay.com/register/person/email/active.htm")

driver.find_element_by_id("username2").send_keys("test@caiwuhao.com")
driver.find_element_by_id("yzm2").send_keys("yzm2")



out=False
while out==False:
    driver.find_element_by_class_name("yzm_img").click()


    t = paramiko.Transport(("192.168.71.129",22))
    t.connect(username = "root", password = " ")
    sftp = paramiko.SFTPClient.from_transport(t)
    remotepath='/google.png'
    localpath='d:/google.png'
    driver.get_screenshot_as_file('d:/google.png')
    sftp.put(localpath,remotepath)
    t.close()
#自动效验验证码
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.71.129", 22,'root', ' ')
    stdin, stdout, stderr = ssh.exec_command('cd /')
    stdin, stdout, stderr = ssh.exec_command("convert /google.png -crop 58x20+585+313 /google1.png")
    stdin, stdout, stderr = ssh.exec_command('tesseract /google1.png /result')
    time.sleep(1)
    stdin, stdout, stderr = ssh.exec_command("cat /result.txt")
    line=stdout.readline().strip()
    line=line[:4]
   # print "["&driver.find_element_by_xpath("//*[@id='register-index-form2']/div[2]/div[2]").text&"}"
    driver.find_element_by_id("yzm2").send_keys(line)
    driver.find_element_by_id("username2").click()
#    time.sleep(1)
    errors= driver.find_element_by_xpath("//*[@id='register-index-form2']/div[2]/div[2]").text
    if len(errors)<5:
        out=True
        break

driver.find_element_by_id("btn_mfhq2").click()
time.sleep(30)
cmd ="python d:/python/mymail1.py>d:/mail.txt"
os.system(cmd)


f = open("d:/mail.txt", "r")
line = f.readline()
f.close()

driver.find_element_by_id("jym2").send_keys(line)
driver.find_element_by_id("btn_submit2").click()
time.sleep(9)
cmd ="c:\userpassword.exe"
os.system(cmd)
time.sleep(9)
driver.find_element_by_id("realname").send_keys(u"蒋明")
driver.find_element_by_id("idcard").send_keys("33010319820329131X")

driver.find_element_by_class_name("btn_next").click()



#560 *465
#

#driver.quit()
#display.stop()

