Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:\Users\Balaji.C\Desktop\pypro\htm.py ===============
Enter - http://py4e-data.dr-chuck.net/comments_534503.html
2439
>>> import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = int(raw_input('Enter count: '))+1
position = int(raw_input('Enter position: '))


tags = soup('a')
tags_lst = list()
for tag in tags:
    needed_tag = tag.get('href', None)
    tags_lst.append(needed_tag)
for i in range(0,count):    
    print 'retrieving: ',tags_lst[position]
    position = position + 1