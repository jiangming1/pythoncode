# coding: UTF-8
#作者 蒋明
#作用 测试kjt登录脚本
#日期 2016-03-09
from selenium import webdriver
import time,os
import paramiko
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

#1001 370
out=False
while out==False:
    driver.find_element_by_id("randImage").click()
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
    stdin, stdout, stderr = ssh.exec_command("convert /google.png -crop 58x20+1001+370 /google1.png")
    stdin, stdout, stderr = ssh.exec_command('tesseract /google1.png /result')
    time.sleep(1)
    stdin, stdout, stderr = ssh.exec_command("cat /result.txt")
    line=stdout.readline().strip()
    line=line[:4]
   #
    driver.find_element_by_id("vercode").send_keys()
    driver.find_element_by_id("kjt_personal_login_login").click()
    errors= driver.find_element_by_xpath("//*[@id='loginForm']/div[5]").text
    if len(errors)<3:
        out=True
        break
driver.get("https://www.kjtpay.com//my/toCashing.htm")
driver.get("https://www.kjtpay.com//my/recharge.htm")
driver.find_element_by_id("money").send_keys("1")
driver.find_element_by_id("bfbtn").click()
#自动登录服务器获取短信验证码
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("www.caiwuhao.com", 22,'root', ' ')
time.sleep(1)
stdin, stdout, stderr = ssh.exec_command("cat /result.txt")
line=stdout.readline().strip()
line=line[:4]
driver.find_element_by_id("qpay_authCode").send_keys("")
time.sleep(9)
#调用usb硬件键盘模拟器输入密码
cmd ="c:\rechargepasswd.exe"
os.system(cmd)
time.sleep(9)
driver.find_element_by_id("kjtpay_submit").click()
#支付成功验证
paycount= driver.find_element_by_xpath("//*[@id='loginForm']/div[5]").text
if paycount=="1":

#driver.quit()