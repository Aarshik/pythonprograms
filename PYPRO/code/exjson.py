import urllib.request,urllib.parse,urllib.error
import json
url='http://py4e-data.dr-chuck.net/comments_885473.json'
print('Retrieving',url)
uh=urllib.request.urlopen(url)
data=uh.read().decode()
print ('Retrieved',len(data),'Characters')
js=json.loads(data)
c=0
for item in js['comments']:
    counts=int(item['count'])
    c+=counts
print('sum',c)
