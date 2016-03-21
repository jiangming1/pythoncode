#!/usr/bin/python
# -*- coding:utf-8 -*-
# cp@chenpeng.info
import paramiko
def MAIN():
    host = “www.caiwuhao.com″
    port = 22132
    user = “root”
    pswd = “jmdjsj903291A″
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, pswd)
    stdin, stdout, stderr = ssh.exec_command(‘ifconfig')
    print stdout.read()
    ssh.close()
#
if __name__=='__main__':
    try:
        MAIN()
    except Exception,e:
        print e