import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import Beautifulsoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
retrieve=ET.fromstring(html)
tree=retrieve.findall('comment/count')
print("count:",len(tree))
c=0
for item in tree:
  print('count',item.find('count').text)
  c=c+1
print('sum',c)
