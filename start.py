import re
from robobrowser import RoboBrowser

b = RoboBrowser(history=True)
b.open('http://itest.info/courses/2')

title = b.select('.headline h2')
print title[0].text

infos = b.select('h4')

for info in infos:
  print info.text