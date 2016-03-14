# coding: UTF-8
#作者 蒋明
#作用 mysql查询表的脚本
#日期 2016-03-09
#!/usr/bin/python
import MySQLdb,time,sys

try:
    tablename='sms_sendmessage_'+time.strftime("%Y%m", time.localtime())
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='x7@cUY^*SR622',db='svr_message',port=3310)
    idsql="SELECT sql_no_cache id from "+tablename+" where tag = 0 and (attime = 0 or attime< unix_timestamp()) ORDER BY id LIMIT 1;"
    countsql="SELECT count(1) from "+tablename+" where tag = 0 and (attime = 0 or attime< unix_timestamp());"
    cur=conn.cursor()
    cur.execute(idsql)
    id1=cur.fetchone()
    time.sleep(1)
    cur.execute(idsql)
    id2=cur.fetchone()
    cur.execute(countsql)
    count=cur.fetchone()
    cur.close()
    if id2==None:
        print "sms list is null"
        sys.exit(0)
    elif count==None:
        print "sms list is null"
        sys.exit(0)
    elif count[0] < 100:
        if id1==None:
            print id2[0],count[0],"sms is ok"
            sys.exit(0)
        else:
            print id1[0],id2[0],count[0],"sms is ok"
            sys.exit(0)
    else:
        print "sms send server is down"
        sys.exit(2)
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
