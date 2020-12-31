import urllib.request
import xml.etree.ElementTree as ET


url = "http://py4e-data.dr-chuck.net/comments_885472.xml"
print ("Retrieving ",url)

xml = urllib.request.urlopen(url).read()
print ("Retrieved: " ,len(xml)," characters")

tree = ET.fromstring(xml)

count =  tree.findall('.//count')
print ("Count: " , len(count))

c = 0

for item in count:
    c+= int(item.text)

print ("Sum:", c)
