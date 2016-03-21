#!/usr/bin/python
import paramiko
t = paramiko.Transport(("www.caiwuhao.com",22132))
t.connect(username = "root", password = "jmdjsj903291A")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/tmp/test.png'
localpath='d:/python/google.png'
sftp.put(localpath,remotepath)
t.close()