import urllib.request
import xml.etree.ElementTree as ET
xml=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.xml')
tree= ET.fromstring(xml)
count= tree.findall('comment/count')
print("count:",len(count))
c=0
for item in count:
  c+=int(item.text)
print('sum',c)
