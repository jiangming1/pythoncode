# coding: UTF-8
#作者 蒋明
#作用 hbase增量恢复脚本
#日期 2016-03-09
import time
import datetime
from datetime import date
import sys
import os
#STR="Basis"
STR="Basis DPM LFLT MA-WEB MAG MGS MNS-ADMIN OPS PKIConsole UESConsole UFS-ADMIN audit counter payment pfs-basis pfs-manager pfs-payment privilege-admin secondary_index staff_info ufs-admin-privileges-conf ufs-user"

tablenames=STR.split()
today=date.today()

for tablename in tablenames:
    backupDst="file:///tmp/back/%s"%(tablename)
    backupSubFolder=backupDst+today.isoformat()+"-full"
    cmd="sudo -u hdfs hbase org.apache.hadoop.hbase.mapreduce.Import %s %s"%(tablename,backupSubFolder)
    print cmd
#    os.system(cmd)
    yesterday=datetime.date.today()- datetime.timedelta(days=1)
    todayTimeStamp=time.mktime(today.timetuple())
    yesTimeStamp=time.mktime(yesterday.timetuple())
    backupSubFolder=backupDst+today.isoformat()
    cmd="sudo -u hdfs hbase org.apache.hadoop.hbase.mapreduce.Import %s %s"%(tablename,backupSubFolder)
    print cmd
#    os.system(cmd)