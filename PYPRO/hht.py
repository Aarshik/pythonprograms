import urllib
from bs4 import  BeautifulSoup

url = input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = int(input('Enter count: '))+1
position = int(input('Enter position: '))


tags = soup('a')
tags_lst = list()
for tag in tags:
    needed_tag = tag.get('href', None)
    tags_lst.append(needed_tag)
for i in range(0,count):
    print ('retrieving: ',tags_lst[position])
    position = position + 1
