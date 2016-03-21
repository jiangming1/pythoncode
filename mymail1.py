# -*- coding: utf-8 -*-
import re
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
aaa="all"
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    global aaa
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
    if (msg.is_multipart()):
        parts = msg.get_payload()

        for n, part in enumerate(parts):
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            aaa=content

email = "test@caiwuhao.com"#raw_input('Email: ')
password ="123456"# raw_input('Password: ')
pop3_server ="pop.caiwuhao.com"# raw_input('POP3 server: ')
server = poplib.POP3(pop3_server)
#server.set_debuglevel(1)
# 认证:
server.user(email)
server.pass_(password)
resp, mails, octets = server.list()
# 获取最新一封邮件, 注意索引号从1开始:
resp, lines, octets = server.retr(len(mails))
# 解析邮件:
msg = Parser().parsestr('\r\n'.join(lines))
# 打印邮件内容:
print_info(msg)
# 慎重:将直接从服务器删除邮件:
# server.dele(len(mails))
# 关闭连接:
server.quit()
ine = "尊敬的test@caiwuhao.com用户您好：<p>  您的注册验证码为rB1G，校验码有效期为24小时，请尽快登录快捷通账户完成注册操作。<br><br>此邮件为系统邮件，请勿直接回复。如有疑问，请拨打4006110909>，或访问快捷通官网：www.kjtpay.com. 【快捷通】</p>"

matchObj = re.match( r'.*(\w\w\w\w).*?24', aaa, re.M|re.I)
if matchObj:
   print matchObj.group(1)

