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
driver.get("https://www.kjtpay.com/register/person/email/active.htm")
driver.find_element_by_id("username2").send_keys("username2@caiwuhao.com")
#driver.get_screenshot_as_file('d:/google.png')
#driver.get_screenshot_as_png()
driver.get_screenshot_as_file('d:/google.png')
driver.find_element_by_id("yzm2").send_keys("yzm2")
driver.find_element_by_id("btn_mfhq2").click()
driver.find_element_by_id("jym2").send_keys("jym2")
# convert google.png -crop 53x21+400+318 1chart-cropped.png
#tesseract 1chart-cropped.png result
driver.find_element_by_id("btn_submit2").click()
time.sleep(5)
#driver.quit()

#ssh_cmd.py
#coding:utf-8

sqldb = localpath+database    //获取database名字
if os.path.exists(sqldb):
    os.chmod(sqldb,stat.S_IRWXU)    //如果database存在，直接改为可读写格式
else:                                         //如果不存在，则远程登录服务器去提取
    child = pexpect.spawn("scp severA@ip:/path/"+database+" "+localpath)   //拷贝到本地目录
    child.expect("serverA@ip's password:")
    child.sendline("password")
    child.interact()
    os.chmod(sqldb,stat.S_IRWXU)

import pexpect

def ssh_cmd(ip, user, passwd, cmd):
ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
r = ''
try:
i = ssh.expect(['password: ', 'continue connecting (yes/no)?'])
if i == 0 :
ssh.sendline(passwd)
elif i == 1:
ssh.sendline('yes')
except pexpect.EOF:
ssh.close()
else:
r = ssh.read()
ssh.expect(pexpect.EOF)
ssh.close()
return r

hosts = '''
192.168.0.12:smallfish:1234:df -h,uptime
192.168.0.13:smallfish:1234:df -h,uptime
'''

for host in hosts.split("/n"):
if host:
ip, user, passwd, cmds = host.split(":")
for cmd in cmds.split(","):
print "-- %s run:%s --" % (ip, cmd)
print ssh_cmd(ip, user, passwd, cmd)