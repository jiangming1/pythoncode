# coding: UTF-8
#作者 蒋明
#作用 测试kjt登录脚本
#日期 2016-03-09
from selenium import webdriver
import time,os
import paramiko
from PIL import Image,ImageEnhance,ImageFilter
import re
import subprocess
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
#图片二值化颜色深的变黑 颜色浅的变白
#适合快捷通的图片 干扰点都比正常的字符串颜色浅.
def binary(f):
    img = f
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    return img

a='2016-3-9 02:00:00'
a_struck_time=time.strptime(a,'%Y-%m-%d %H:%M:%S')
print time.mktime(a_struck_time)
print time.time()
runtime=time.mktime(a_struck_time)
while runtime>time.time():
    time.sleep(6)
    print "wait"
driver=webdriver.Ie('d:/IEDriverServer.exe')
driver.get("https://www.kjtpay.com/index.htm?")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("13858101782@qq.com")
driver.find_element_by_id("checkbox_safepw").click()
driver.find_element_by_id("unSafePwInputOut").send_keys("jmdjsj903291A")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.71.129", 22,'root', ' ')
t = paramiko.Transport(("192.168.71.129",22))
t.connect(username = "root", password = " ")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/google.png'
localpath='d:/googleb.png'
#1001 370
out=False
while out==False:
#    driver.find_element_by_id("randImage").click()
#    time.sleep(1)
    driver.get_screenshot_as_file('d:/google.png')
    im = Image.open('d:/google.png')
    region=(1074,306,1074+72,306+28)
    im=im.crop(region)
    im=binary(im)
    im.save('d:/googleb.png')
    im.save('d:/a/'+time.time().__str__()+".png")

    sftp.put(localpath,remotepath)
#自动效验验证码
    stdin, stdout, stderr = ssh.exec_command('tesseract /google.png /result &> /dev/null && cat /result.txt ')
    line=stdout.readline()
    line=line[:4]
    print line
    if line=="":
        line="aaa"
    driver.find_element_by_id("vercode").clear()
    driver.find_element_by_id("vercode").send_keys(line)
    driver.find_element_by_id("username").click()
    time.sleep(0.5)
    try:
        errors= driver.find_element_by_xpath('//*[@id="login_form"]/div[5]').text
        print errors
        if len(errors)<3:
            break
    except:
        break
driver.find_element_by_id("kjt_personal_index_login").click()
time.sleep(3)

#driver.find_element_by_xpath('//*[@id="kjt_personal_index_login"]').click()
#driver.get("https://www.kjtpay.com//my/toCashing.htm")
driver.get("https://www.kjtpay.com//my/recharge.htm")
time.sleep(3)
driver.find_element_by_id("money").send_keys("1")
driver.find_element_by_id("mfbtn").click()
cmd ="c:/rechargepasswd.exe"

child = subprocess.Popen(cmd,shell=True)
time.sleep(20)
child.kill()
#自动登录服务器获取短信验证码

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("www.caiwuhao.com", 22132,'root', 'jmdjsj903291A')
stdin, stdout, stderr = ssh.exec_command("cat /alidata/www/888/a/test.txt")
line=stdout.readline().strip()
matchObj = re.match( r'.*(\d\d\d\d\d\d).*', line, re.M|re.I)
print "login"
if matchObj:
   print matchObj.group(1)
   driver.find_element_by_id("qpay_authCode").send_keys(matchObj.group(1))

kjtcount=driver.find_element_by_class_name("order_amount").text
print kjtcount
#https://cash.kjtpay.com/result/payNotifyResult.htm?notifyToken=C2310861&memberType=1&token=C2310841
driver.find_element_by_id("kjtpay_submit").click()
time.sleep(11)
#driver.quit()
